import json
import requests

from alt_py.storage import alt_storage
from alt_py.storage import location as alt_location
from alt_py import config


class FirebaseStorage(alt_storage.AltStorage):
    """Firebase storage"""

    def __init__(self):
        alt_storage.AltStorage.__init__(self)
        config_setup = config.Config()
        self.firebase_host = config_setup.firebase_host
        self.firebase_path = config_setup.firebase_path

    def get_hosts(self):
        url = 'https://{}{}.json'.format(self.firebase_host, self.firebase_path)
        json_data = self.make_request_(url, 'get')
        locations = []
        if json_data is not None:
            for key in json_data.keys():
                location = alt_location.Location()
                location.to_location(json_data[key])
                locations.append(location)
        return sorted(locations, key=lambda loc: loc.name)

    def update_host(self, location):
        url = 'https://{}{}/{}.json'.format(self.firebase_host,
                                            self.firebase_path, location.name)
        json_data = self.make_request_(url, 'patch')
        if json_data is not None:
            return True
        else:
            return False

    def remove_host(self, location):
        url = 'https://{}{}/{}.json'.format(self.firebase_host,
                                            self.firebase_path, location.name)
        response = self.make_request_(url, 'delete')
        if response.status_code == 200:
            return True
        else:
            return False

    def make_request_(self, url, caller):
        if caller == 'get':
            response = requests.get(url)
            return json.loads(response.text)
        elif caller == 'patch':
            response = requests.patch(url)
            return json.loads(response.text)
        elif caller == 'delete':
            return requests.delete(url)
