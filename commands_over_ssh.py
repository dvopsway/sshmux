import subprocess
import pexpect
import sys
import tempfile
import getpass

def ssh(host, cmd ,user, password, timeout=30, bg_run=False):
    fname = tempfile.mktemp()
    fout = open(fname, 'w')
    options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
    if bg_run:
        options += ' -f'
    ssh_cmd = 'ssh %s@%s %s "%s"' % (user, host, options, cmd)                  
    child = pexpect.spawn(ssh_cmd, timeout=timeout)
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

#Executing and fetching output
servers = list(sys.argv[1:])
username = raw_input("SSH Username : ")
password = getpass.getpass()
print "Enter your commands below:\n"
command = raw_input(">> ")
while command != "quit":
    for each in servers:
        output = ssh(each,command,username,password)
        print each + " : "  
	for line in output.split('\n')[1:]:
		print line
    command = str(raw_input(">> "))
print "session closed"
