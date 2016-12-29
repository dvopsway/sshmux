from __future__ import print_function
from builtins import input

import pexpect
import tempfile
import click
import socket
import multiprocessing
from getpass import getpass
from os import path, unlink, environ


def ssh(host, cmd, user, password, key, timeout=10, bg_run=False):
    """connect to host via ssh"""
    output_file = tempfile.NamedTemporaryFile(delete=False)
    option = ["-q", "-oStrictHostKeyChecking=no",
              "-oUserKnownHostsFile=/dev/null"]
    if password:
        option.append("-oPubkeyAuthentication=no")
    if not password:
        option.append("-o PreferredAuthentications=publickey")
    if bg_run:
        option.append('-f')

    options = " ".join(option)
    ssh_cmd = None
    if not password:
        ssh_cmd = 'ssh -i {0} {1}@{2} {3} "{4}"'.format(
            key, user, host, options, cmd)
    elif password:
        ssh_cmd = 'ssh {0}@{1} {2} "{3}"'.format(user, host, options, cmd)

    child = pexpect.spawn(ssh_cmd, timeout=timeout)
    if password:
        child.expect(['Password for'])
        child.sendline(password)

    child.logfile = output_file
    child.expect(pexpect.EOF)
    child.close()
    output_file.close()

    # BUG(rjrhaverkamp): U mode is deprecated
    read_file = open(output_file.name, 'rU')
    stdout = read_file.read()
    output_file.close()
    read_file.close()
    unlink(output_file.name)

    if child.exitstatus != 0:
        raise Exception(stdout)
    print_output(host, stdout)
    return stdout


def print_output(server, output):
    print(server + ":\n")
    for line in output.split('\n')[1:]:
        print(line)


def validate_hostname(ctx, param, value):
    "validate hostname / IP address"
    for address in value:
        try:
            socket.inet_aton(address)
        except socket.error:
            try:
                socket.gethostbyaddr(address)
            except socket.gaierror:
                raise click.BadParameter(
                    '{0} - Address is not valid'.format(address))
    return value


def validate_pass(value):
    """validate password lenght"""
    if len(value) == 0 or len(value) > 100:
        raise click.BadParameter('password length is not valid')
    return value


def validate_user(ctx, param, value):
    """validate username length"""
    if len(value) == 0 or len(value) > 100:
        raise click.BadParameter('username length is not valid')
    return value


def validate_key(ctx, param, value):
    """validate that key exists."""
    if path.exists(value):
        return value
    else:
        raise click.BadParameter('{0} file doesn\'t exist'.format(value))


@click.command()
@click.option('--hostname', '-h', callback=validate_hostname, multiple=True,
              help='IP address or hostname')
@click.option('--username', '-u', callback=validate_user, default='',
              help='ssh username')
@click.option('--password', '-p', default=False, help='ssh password')
@click.option('--key', '-k', default=environ['HOME'] + '/.ssh/id_rsa',
              help='ssh private key', callback=validate_key)
def main(hostname, username, password, key):
    """Open ssh session with each ip and execute a command from stdin."""
    if password:
        password = getpass()
        password = validate_pass(password)
    print("Enter your commands below:\n")
    command = input("sshmux > ")

    while command != "quit":
        procs = []
        for server in hostname:
            procs.append(multiprocessing.Process(
                target=ssh, args=(server, command, username, password, key)))
        for proc in procs:
            proc.start()
        for proc in procs:
            proc.join()
        command = str(input("sshmux > "))
    print("session closed")


if __name__ == '__main__':
    main()
