from abc import ABCMeta, abstractmethod


class AltStorage:
    """The storage base class."""

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_hosts(self):
        """Get a list of locations from storage."""
        pass

    @abstractmethod
    def update_host(self, location):
        """Update a location to storage. Returns a boolean on if it was successful."""
        pass

    @abstractmethod
    def remove_host(self, location):
        """Remove a location from storage. Returns boolean on if it was successful."""
        pass
