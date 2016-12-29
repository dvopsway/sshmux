import click
import unittest
from sshmux import validate
import pprint

from click.testing import CliRunner

class TestValidations(unittest.TestCase):
    @click.command()
    @click.option('--hostname', '-h', callback=validate.validate_hostname, multiple=True, help='IP address or hostname') # NOQA
    def check_hostname(hostname):
        click.echo('sucess')
    
    def test_hostname_check(self):
        runner = CliRunner()
        result = runner.invoke(self.check_hostname, ['-h', '127.0.0.1'])
        self.assertEqual('sucess\n', result.output)

    def test_hostname_fail(self):
        runner = CliRunner()
        result = runner.invoke(self.check_hostname, ['-h', 'wrong_host_name'])
        self.assertNotEqual(result.exit_code, 0)
     

if __name__ == '__main__':
    unittest.main()
