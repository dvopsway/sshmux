from __future__ import print_function
from builtins import input

import click
import multiprocessing
from sshmux import validate
from sshmux.ssh import ssh
from getpass import getpass
from os import environ


@click.command()
@click.option('--hostname', '-h', callback=validate.validate_hostname,
              multiple=True, help='IP address or hostname')
@click.option('--username', '-u', callback=validate.validate_user, default='',
              help='ssh username')
@click.option('--password', '-p', default=False, help='ssh password')
@click.option('--key', '-k', default=environ['HOME'] + '/.ssh/id_rsa',
              help='ssh private key')
def main(hostname, username, password, key):
    """Open ssh session with each ip and execute a command from stdin."""
    if not password:
        key = validate.validate_key(key)
    if password:
        password = getpass()
        password = validate.validate_pass(password)
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
