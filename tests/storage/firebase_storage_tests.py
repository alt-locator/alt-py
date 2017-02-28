from context import alt_py
from alt_py.storage import firebase_storage

import unittest


class FirebaseStorageTest(unittest.TestCase):
    """Firebase storage tests"""

    def test_get_hosts(self):
      firebase_test = firebase_storage.FirebaseStorage()
      firebase_test.firebase_host = 'alt-github.firebaseio.com'
      firebase_test.firebase_path = '/test/read/hosts'
      get_hosts = firebase_test.get_hosts()
    
    def test_update_host(self):
      pass
    
    def test_remove_host(self):
      pass


if __name__ == '__main__':
    unittest.main()
