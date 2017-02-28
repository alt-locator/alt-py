from alt_py.storage.alt_storage import AltStorage


class MockStorage(AltStorage):
    """Mock storage saves information to memory"""

    def __init__(self):
        AltStorage.__init__(self)
        self.hosts = []

    def get_hosts(self):
        return self.hosts

    def update_host(self, location):
        for host in self.hosts:
            if host.name == location.name:
                index = self.hosts.index(host)
                self.hosts[index] = location
                return True
        self.hosts.append(location)
        return True

    def remove_host(self, location):
        for host in self.hosts:
            if host.name == location.name:
                self.hosts.remove(location)
                return True
        return False
