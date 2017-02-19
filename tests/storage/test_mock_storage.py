from context import alt_py

import unittest


class TestMockStorage(unittest.TestCase):
    """Mock storage tests"""

    def test_get_hosts(self):
        mockStorage = alt_py.storage.mock_storage.MockStorage()
        getHosts = mockStorage.get_hosts()
        self.assertEqual(getHosts, ['get hosts'])

    def test_update_host(self):
        mockStorage = alt_py.storage.mock_storage.MockStorage()
        location = alt_py.storage.location.Location()
        updateHost = mockStorage.update_host(location)
        self.assertTrue(updateHost)

    def test_remove_host(self):
        mockStorage = alt_py.storage.mock_storage.MockStorage()
        location = alt_py.storage.location.Location()
        removeHost = mockStorage.remove_host(location)
        self.assertTrue(removeHost)


if __name__ == '__main__':
    unittest.main()
