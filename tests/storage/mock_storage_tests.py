from context import alt_py
from alt_py.storage import location
from alt_py.storage import mock_storage

import unittest


class MockStorageTest(unittest.TestCase):
    """Mock storage tests"""

    def test_get_hosts(self):
        mock_test = mock_storage.MockStorage()
        location_test = location.Location()
        location_test.name = 'foobar'
        mock_test.hosts.append(location_test)

        get_hosts = mock_test.get_hosts()
        self.assertEqual(len(get_hosts), 1)
        self.assertEqual(get_hosts[0].name, location_test.name)

    def test_update_host(self):
        mock_test = mock_storage.MockStorage()
        location_test = location.Location()
        location_test.name = 'foobar'

        update_host = mock_test.update_host(location_test)
        self.assertTrue(update_host)
        self.assertEqual(len(mock_test.hosts), 1)
        self.assertEqual(mock_test.hosts[0].name, location_test.name)

    def test_remove_host(self):
        mock_test = mock_storage.MockStorage()
        location_test = location.Location()
        location_test.name = 'foobar'
        mock_test.hosts.append(location_test)

        remove_host = mock_test.remove_host(location_test)
        self.assertTrue(remove_host)
        self.assertEqual(len(mock_test.hosts), 0)


if __name__ == '__main__':
    unittest.main()
