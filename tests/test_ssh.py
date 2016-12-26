import unittest
from os import environ

from sshmux import ssh

class TestSSH(unittest.TestCase):
    def test_ssh_output(self):
        output = ssh.ssh(environ['sshmux_test_host'], 'echo "hello"', environ['sshmux_test_user'], '', environ['sshmux_test_key'])
        self.assertEqual(output, 'hello\r\n')

if __name__ == '__main__':
    unittest.main()