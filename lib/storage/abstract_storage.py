"""An abstract storage class for alternative location tool."""
import abc


class AbstractStorage(object):
  """The storage abstract class."""

  __metaclass__ = abc.ABCMeta

  def __init__(self, config):
    """Initializes the storage class.

    Args:
      config: (config) A configuration object.
    """
    self.config = config

  @abc.abstractmethod
  def GetLocations(self):
    """Get a list of locations from storage.
    
    Returns:
      An array of locations.
    """
    pass

  @abc.abstractmethod
  def UpdateLocation(self):
    """Update a location to storage.
    
    Returns:
      A boolean of the result.
    """
    pass
  
  @abc.abstractmethod
  def RemoveLocation(self):
    """Remove a location from storage.

    Returns:
      A boolean of the result.
    """