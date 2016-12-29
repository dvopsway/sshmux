import click
import socket
from os import path


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


def validate_key(value):
    """validate that key exists."""
    if path.exists(value):
        return value
    else:
        raise click.BadParameter('{0} file doesn\'t exist'.format(value))
