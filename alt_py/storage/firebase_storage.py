import json
import requests

from alt_py.storage.alt_storage import AltStorage
from alt_py import config


class FirebaseStorage(AltStorage):
    """Firebase storage"""

    def __init__(self):
        AltStorage.__init__(self)
        self.config = config.Config()

    def get_hosts(self):
        url = 'https://' + self.config.firebase_host + self.config.firebase_path + '.json'
        req = requests.get(url)
        json_data = json.loads(req.text)
        if json_data is not None:
            print json_data

    def update_host(self, location):
        pass

    def remove_host(self, location):
        pass
