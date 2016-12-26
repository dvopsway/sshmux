import pexpect
import tempfile
import click


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


@click.command()
@click.option('--ip', '-i', multiple=True, help='IP address')
@click.option('--username', '-u', default='', help='ssh username')
@click.option('--password', '-p', default='', help='ssh password')
@click.option('--key', '-k', default='', help='ssh private key')
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
