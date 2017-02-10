from context import alt_py

import unittest

class TestMockStorage(unittest.TestCase):
    '''
    Mock storage tests
    '''

    def test_getHosts(self): 
        mockStorage = alt_py.storage.mock_storage.MockStorage()
        getHosts = mockStorage.getHosts()
        self.assertEqual(getHosts, ['get hosts'])

    def test_updateHost(self):
        mockStorage = alt_py.storage.mock_storage.MockStorage()
        location = alt_py.storage.location.Location()
        updateHost = mockStorage.updateHost(location)
        self.assertTrue(updateHost)

    def test_removeHost(self):
        mockStorage = alt_py.storage.mock_storage.MockStorage()
        location = alt_py.storage.location.Location()
        removeHost = mockStorage.removeHost(location)
        self.assertTrue(removeHost)


if __name__ == '__main__':
    unittest.main()