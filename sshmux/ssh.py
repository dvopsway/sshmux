import pexpect
import tempfile
import click
import socket
import os.path


def ssh(host, cmd, user, password, key, timeout=30, bg_run=False):
    fname = tempfile.mktemp()
    fout = open(fname, 'w')
    option = []
    option.append("-q")
    option.append("-oStrictHostKeyChecking=no")
    option.append("-oUserKnownHostsFile=/dev/null")
    if password != "":
        option.append("-oPubkeyAuthentication=no")
    options = " ".join(option)
    if bg_run:
        options += ' -f'
    ssh_cmd = None
    if password == "":
        ssh_cmd = 'ssh -i %s %s@%s %s "%s"' % (key, user, host, options, cmd)
    else:
        ssh_cmd = 'ssh %s@%s %s "%s"' % (user, host, options, cmd)
    child = pexpect.spawn(ssh_cmd, timeout=timeout)
    if password != "":
        child.expect(['password: '])
        child.sendline(password)
    child.logfile = fout
    child.expect(pexpect.EOF)
    child.close()
    fout.close()
    fin = open(fname, 'r')
    stdout = fin.read()
    fin.close()
    if 0 != child.exitstatus:
        raise Exception(stdout)
    return stdout


def validate_ips(ctx, param, value):
    for each in value:
        try:
            socket.inet_aton(each)
        except socket.error:
            raise click.BadParameter('%s - IP address is not valid' % each)
    return value


def validate_pass(ctx, param, value):
    if len(value) == 0 or len(value) > 100:
        raise click.BadParameter('password length is not valid')
    return value


def validate_user(ctx, param, value):
    if len(value) == 0 or len(value) > 100:
        raise click.BadParameter('username length is not valid')
    return value


def validate_key(ctx, param, value):
    if os.path.exists(value):
        return value
    else:
        raise click.BadParameter('%s file doesn\'t exist' % value)


@click.command()
@click.option('--ip', '-i', callback=validate_ips, multiple=True, help='IP address')
@click.option('--username', '-u', callback=validate_user, default='', help='ssh username')
@click.option('--password', '-p', default='', help='ssh password')
@click.option('--key', '-k', callback=validate_key, default='', help='ssh private key')
def sshmux(ip, username, password, key):
    servers = ip
    uname = username
    upass = password
    print "Enter your commands below:\n"
    command = raw_input("sshmux > ")
    while command != "quit":
        for each in servers:
            output = ssh(each, command, uname, upass, key)
            print each + " : "
            for line in output.split('\n')[1:]:
                print line
        command = str(raw_input("sshmux > "))
    print "session closed"


if __name__ == '__main__':
    sshmux()
