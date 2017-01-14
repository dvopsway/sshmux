from __future__ import print_function

from subprocess import Popen, PIPE, STDOUT
from sshmux.errors import MuxError


def print_output(server, output):
    """parse ssh output and print to stdout"""
    print(server + ":\n")
    for line in output.split('\n')[1:]:
        print(line)


def ssh(host, cmd, user, key, wait=10, bg_run=False):
    """connect to host via ssh"""
    option = ["-q", "-oStrictHostKeyChecking=no",
              "-oUserKnownHostsFile=/dev/null", "-o PreferredAuthentications=publickey"]
    if bg_run:
        option.append('-f')
    options = " ".join(option)
    ssh_cmd = None
    ssh_cmd = 'ssh -i {0} {1}@{2} {3} "{4}"'.format(
        key, user, host, options, cmd)

    run = Popen(ssh_cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    run.wait()
    
    if run.returncode != 0:
        raise MuxError("failed to run {0} on {1}. Exited with: {2}".format(
            cmd, host, run.returncode))

    output, _ = run.communicate()
    print(run.returncode)
    print_output(host, output.decode("utf-8"))
    return output.decode("utf-8")
