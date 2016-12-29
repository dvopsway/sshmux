from __future__ import print_function

import pexpect
import tempfile
from os import unlink


def print_output(server, output):
    """parse ssh output and print to stdout"""
    print(server + ":\n")
    for line in output.split('\n')[1:]:
        print(line)


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
