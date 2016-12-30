
# sshmux ![travis status](https://travis-ci.org/dvopsway/sshmux.svg?branch=master) [![codecov](https://codecov.io/gh/dvopsway/sshmux/branch/master/graph/badge.svg)](https://codecov.io/gh/dvopsway/sshmux) [![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/dvopsway/sshmux) [![Join the chat at https://gitter.im/dvopsway/sshmux](https://badges.gitter.im/dvopsway/sshmux.svg)](https://gitter.im/dvopsway/sshmux?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Run commands over ssh on multiple servers, sshmux can help you in debugging stuff on multiple servers parallelly, continue reading to understand how it works.

## Installation :

Use pip to install sshmux (will be available soon)

```
pip install sshmux
```

#### Alternate installation

You can also compile from source, just clone the repo and run the command below:

```
python setup.py install
```

## Getting Started :

sshmux can work with multiple IPs or hostnames

To get started, start with --help
```
sshmux --help
Usage: sshmux [OPTIONS]

Options:
  -h, --hostname TEXT  hostname or IP address
  -u, --username TEXT  ssh username
  -p, --password BOOL  ssh password
  -k, --key      TEXT  ssh private key
  --help               Show this message and exit.
```

Check the example usage to get started

## Example Usage :

```
➜  ~  sshmux -h 10.0.0.3 -h 10.0.0.4 -u "ec2-user" -k ~/awstempkey.pem
Enter your commands below:

sshmux > ls -al /tmp
10.0.0.3 :
drwxrwxrwt  5 root     root     4096 Dec 23 11:55 .
dr-xr-xr-x 30 root     root     4096 Dec 20 09:05 ..
drwxr-xr-x  2 root     root     4096 Dec 23 11:43 hsperfdata_root
drwxrwxrwt  2 root     root     4096 Oct 26 10:35 .ICE-unix
drwx------  2 ec2-user ec2-user 4096 Dec 23 11:55 ssh-J4yIqFVoEC

10.0.0.4 :
drwxrwxrwt  5 root     root     4096 Dec 23 11:56 .
dr-xr-xr-x 30 root     root     4096 Dec 20 09:12 ..
drwxr-xr-x  2 root     root     4096 Dec 23 11:30 hsperfdata_root
drwxrwxrwt  2 root     root     4096 Sep 27 13:10 .ICE-unix
drwx------  2 ec2-user ec2-user 4096 Dec 23 11:56 ssh-lN3JYqQep7

sshmux > quit
```

## Password usage:

sshmux default is to use an ssh private key located in `~/.ssh/id_rsa`.
If you want to use a password you need to add `-p True` or
 `--password True` to the command. sshmux will then ask you for a password.

## Contributing
if your code doesn't follow the contribution guidelines it won't be merged

1. read [CONTRIBUTING.md](https://github.com/dvopsway/sshmux/blob/master/CONTRIBUTING.md)
2. Fork it!
3. Create your feature branch: `git checkout -b my-new-feature`
4. stage your feature: `git add <changed_file>`
5. Commit your changes: `git commit -m 'feat: add new feature' -m 'add my-new-feature, use it as: my-new-feautre(args)' -m 'closes #26'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request :D
