import unittest
import os
from Hosts import Hosts

hostsFilepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt');
hosts = Hosts(hostsFilepath)


class TestHostsMethods(unittest.TestCase):

    def test_default_value(self):
        self.assertEqual(hosts.getHosts(), [])

    def test_adding_host(self):
        hosts.addHost('google.com')
        self.assertEqual(hosts.getHosts(), ['google.com'])
        hosts.deleteHost('google.com')

    def test_deleting_host(self):
        hosts.addHost('google.com')
        hosts.deleteHost('google.com')
        self.assertEqual(hosts.getHosts(), [])

    def test_disable_host(self):
        hosts.addHost('google.com')
        hosts.disableHost('google.com')
        self.assertEqual(hosts.hosts, [['127.0.0.1', 'google.com', False]])
        hosts.deleteHost('google.com')

    def test_enable_host(self):
        hosts.addHost('google.com')
        hosts.disableHost('google.com')
        hosts.enableHost('google.com')
        self.assertEqual(hosts.hosts, [['127.0.0.1', 'google.com', True]])
        hosts.deleteHost('google.com')

    def test_deleting_all(self):
        hosts.addHost('google.com')
        hosts.addHost('facebook.com')
        hosts.deleteAllHosts()
        self.assertEqual(hosts.getHosts(), [])


if __name__ == '__main__':
    unittest.main()
