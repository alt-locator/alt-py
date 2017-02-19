from alt_py.storage.alt_storage import AltStorage


class MockStorage(AltStorage):
    """Mock storage saves information to memory"""

    def __init__(self):
        AltStorage.__init__(self)

    def get_hosts(self):
        return ['get hosts']

    def update_host(self, location):
        return True

    def remove_host(self, location):
        return True
