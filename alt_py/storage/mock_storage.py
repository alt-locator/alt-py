from alt_storage import AltStorage

class MockStorage(AltStorage):

    def __init__(self):
        pass

    def getHosts(self):
        return ['get hosts']

    def updateHost(self, location):
        return True

    def removeHost(self, location):
        return True

