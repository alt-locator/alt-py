import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

import abstract_storage
import location


class FirebaseStorage(abstract_storage.AbstractStorage):

  def __init__(self, config):
    """Initializes the firebase storage admin with credentials.

    Args:
      config: (config) The configuraton object containing firebase related values to authenticate.
    """
    abstract_storage.AbstractStorage.__init__(self, config)
    self.firebaseio_base_path = config.firebaseio_base_path
    self.SetCredentials(config.firebaseio_url, config.firebaseio_service_account_json)

  def SetCredentials(self, firebaseio_url, service_account_key_json):
    """Sets the credentials for the firebase admin db.

    Args:
      firebase_url: (string) The firebaseio url.
      service_account_key_json: (string) Full path to the service account key json file.
    """
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(service_account_key_json)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
      'databaseURL': firebaseio_url
    })

  def GetLocations(self):
    """Get a list of locations from storage.
    
    Returns:
      An array of locations.
    """
    locations = []
    ref = db.reference(self.firebaseio_base_path)
    json_locations = json.loads(json.dumps(ref.get()))
    for key in json_locations.keys():
      my_location = location.Location(key)
      my_location.ToLocation(json_locations[key])
      locations.append(my_location)
    return locations


  def UpdateLocation(self, location):
    """Update a location to storage.
    
    Returns:
      A boolean of the result.
    """
    print 'update location: ' + self.firebaseio_base_path + '/' + location.name
    location_ref = db.reference(self.firebaseio_base_path + '/' + location.name)
    location_ref.set(location.ToJson())
  
  def RemoveLocation(self, location):
    """Remove a location from storage.

    Returns:
      A boolean of the result.
    """
    print 'remove location: ' + self.firebaseio_base_path + '/' + location.name
    location_ref = db.reference(self.firebaseio_base_path + '/' + location.name)
    location_ref.delete()
    