"""Configuration for alternative location tool."""
import os
import platform

_LOCATION_NAME = 'ALT_LOCATION_NAME'
_FIREBASEIO_URL = 'ALT_FIREBASEIO_URL'
_FIREBASEIO_BASE_PATH = 'ALT_FIREBASEIO_BASE_PATH'
_FIREBASEIO_SERVICE_ACCOUNT_JSON = 'ALT_FIREBASEIO_SERVICE_ACCOUNT_JSON'
_FIREBASEIO_DEFAULT_URL = 'https://alt-github.firebaseio.com' 
_FIREBASEIO_DEFAULT_BASE_PATH = '/alt'

class Config(object):
  """Configuration settings."""

  def __init__(self):
    """Creates a config with default values or from environment variables."""
    if os.environ.has_key(_LOCATION_NAME):
      self.location_name = os.environ.get(_LOCATION_NAME)
    else:
      self.location_name = platform.node()

    if os.environ.has_key(_FIREBASEIO_URL):
      self.firebaseio_url = os.environ.get(_FIREBASEIO_URL)
    else:
      self.firebaseio_url = _FIREBASEIO_DEFAULT_URL
    
    if os.environ.has_key(_FIREBASEIO_BASE_PATH):
      self.firebaseio_base_path = os.environ.get(_FIREBASEIO_BASE_PATH)
    else:
      self.firebaseio_base_path = _FIREBASEIO_DEFAULT_BASE_PATH
    
    if os.environ.has_key(_FIREBASEIO_SERVICE_ACCOUNT_JSON):
      self.firebaseio_service_account_json = os.environ.get(_FIREBASEIO_SERVICE_ACCOUNT_JSON)