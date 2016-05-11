# remote_command_execution
run commands over ssh on multiple servers by passing servers as a command line parameter

usage :

```
[root@10.56.45.63 notebooks]# python commands_over_ssh.py 10.56.45.64 10.56.45.65
SSH Username : root
Password:
Enter your commands below:

>> uname -a
10.56.45.64 :
Linux TEST1 2.6.32-504.30.3.el6.x86_64 #1 SMP Wed Jul 15 10:13:09 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

10.56.45.65 :
Linux TEST2 2.6.32-220.el6.x86_64 #1 SMP Tue Dec 6 19:48:22 GMT 2011 x86_64 x86_64 x86_64 GNU/Linux

>> ls /tmp
10.56.45.64 :
file1
file2

10.56.45.65 :
file3.txt

>> quit
session closed

```
