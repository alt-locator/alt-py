import unittest
from mock_storage import MockStorage
from location import Location

class TestMockStorage(unittest.TestCase):
    '''
    Mock storage tests
    '''

    def test_getHosts(self): 
        mockStorage = MockStorage()
        getHosts = mockStorage.getHosts()
        self.assertEqual(getHosts, ['get hosts'])

    def test_updateHost(self):
        mockStorage = MockStorage()
        location = Location()
        updateHost = mockStorage.updateHost(location)
        self.assertTrue(updateHost)

    def test_removeHost(self):
        mockStorage = MockStorage()
        location = Location()
        removeHost = mockStorage.removeHost(location)
        self.assertTrue(removeHost)


if __name__ == '__main__':
    unittest.main()