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
        req = requests.get(url)
        json_data = json.loads(req.text)
        locations = []
        if json_data is not None:
            for key in json_data.keys():
                location = alt_location.Location()
                location.to_location(json_data[key])
                locations.append(location)
        return sorted(locations)

    def update_host(self, location):
        url = 'https://{}{}/{}.json'.format(self.firebase_host, self.firebase_path, location.name)
        req = requests.patch(url, location.to_json())
        json_data = json.loads(req.text)
        location = alt_location.Location()
        location.to_location(json_data)
        return location

    def remove_host(self, location):
        pass
