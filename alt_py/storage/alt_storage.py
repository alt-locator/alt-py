from abc import ABCMeta, abstractmethod

class AltStorage:
    '''
    The storage base class.
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def getHosts(self):
        '''
        Get a list of locations from storage.
        '''
        pass
    
    @abstractmethod
    def updateHost(self, location):
        '''
        Update a location to storage. Returns a boolean on if it was successful.
        '''
        pass
    
    @abstractmethod
    def removeHost(self, location):
        '''
        Remove a location from storage. Returns boolean on if it was successful.
        '''
        pass
