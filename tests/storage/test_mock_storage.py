from context import alt_py
from alt_py import storage

import unittest


class TestMockStorage(unittest.TestCase):
    """Mock storage tests"""

    def test_get_hosts(self):
        mock_storage = storage.mock_storage.MockStorage()
        location = storage.location.Location()
        location.name = 'foobar'
        mock_storage.hosts.append(location)

        get_hosts = mock_storage.get_hosts()
        self.assertEqual(len(get_hosts), 1)
        self.assertEqual(get_hosts[0].name, 'foobar')

    def test_update_host(self):
        mock_storage = storage.mock_storage.MockStorage()
        location = storage.location.Location()
        location.name = 'foobar'

        update_host = mock_storage.update_host(location)
        self.assertTrue(update_host)
        self.assertEqual(len(mock_storage.hosts), 1)
        self.assertEqual(mock_storage.hosts[0].name, 'foobar')

    def test_remove_host(self):
        mock_storage = storage.mock_storage.MockStorage()
        location = storage.location.Location()
        location.name = 'foobar'
        mock_storage.hosts.append(location)

        remove_host = mock_storage.remove_host(location)
        self.assertTrue(remove_host)
        self.assertEqual(len(mock_storage.hosts), 0)


if __name__ == '__main__':
    unittest.main()
