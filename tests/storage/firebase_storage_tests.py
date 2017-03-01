from context import alt_py
from alt_py.storage import firebase_storage
from alt_py.storage import location as alt_location

import unittest


class FirebaseStorageTest(unittest.TestCase):
    """Firebase storage tests"""

    def test_get_hosts(self):
      firebase_test = firebase_storage.FirebaseStorage()
      firebase_test.firebase_host = 'alt-github.firebaseio.com'
      firebase_test.firebase_path = '/test/read/hosts'
      get_hosts = firebase_test.get_hosts()

      self.assertEqual(len(get_hosts), 2)
      self.assertEqual(get_hosts[0].name, 'foo')
      self.assertEqual(get_hosts[0].external_ip_address, 'http://20.20.20.20')
      self.assertEqual(get_hosts[0].local_ip_address, 'http://10.0.0.1')
      self.assertEqual(get_hosts[0].mac_address, '1a:2b:3c:4d')
      self.assertEqual(len(get_hosts[0].ports), 1)
      self.assertEqual(get_hosts[0].ports[0], 8080)
      self.assertEqual(get_hosts[0].timestamp, 1400000000)
      self.assertEqual(get_hosts[1].name, 'bar')
      self.assertIsNone(get_hosts[1].external_ip_address)
      self.assertIsNone(get_hosts[1].local_ip_address)
      self.assertIsNone(get_hosts[1].mac_address)
      self.assertIsNone(get_hosts[1].ports)
      self.assertEqual(get_hosts[1].timestamp, 1500000000)
    
    def test_update_host(self):
      firebase_test = firebase_storage.FirebaseStorage()
      firebase_test.firebase_host = 'alt-github.firebaseio.com'
      firebase_test.firebase_path = '/test/write/hosts'
      location = alt_location.Location()
      location.name = 'baz'
      update_host = firebase_test.update_host(location)
      self.assertEqual(update_host.name, 'baz')
      self.assertIsNone(update_host.external_ip_address)
      self.assertIsNone(update_host.local_ip_address)
      self.assertIsNone(update_host.mac_address)
      self.assertIsNone(update_host.ports)
      self.assertIsNone(update_host.timestamp)
      
    def test_remove_host(self):
      pass


if __name__ == '__main__':
    unittest.main()
