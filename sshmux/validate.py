import click
import socket
from os import path


def validate_hostname(ctx, param, hostname):
    "validate hostname / IP address"
    for address in hostname:
        try:
            socket.inet_aton(address)
        except socket.error:
            try:
                socket.gethostbyaddr(address)
            except socket.gaierror:
                raise click.BadParameter(
                    '{0} - Address is not valid'.format(address))
    return hostname


def validate_pass(password):
    """validate password lenght"""
    if len(password) == 0 or len(password) > 100:
        raise click.BadParameter('password length is not valid')
    return password


def validate_user(ctx, param, username):
    """validate username length"""
    if len(username) == 0 or len(username) > 100:
        raise click.BadParameter('username length is not valid')
    return username


def validate_key(key_path):
    """validate that key exists."""
    if path.exists(key_path):
        return key_path
    else:
        raise click.BadParameter('{0} file doesn\'t exist'.format(key_path))
