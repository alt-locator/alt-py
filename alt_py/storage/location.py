class Location(object):
    """The location model that includes network information."""

    def __init__(self, name=None):
        # The Local (Internal) IP Address. If your computer is connected to a router with default
        # settings, that router will automatically assign a local IP address to your computer. Your
        # local IP address is hidden from the outside world and used only inside your private
        # network.
        #
        # https://goo.gl/txEmRd
        self.local_ip_address = None

        # The External (Public) IP Address. The Internet Service Provider (ISP) assigns you an
        # external IP address when you connect to the Internet. When your browser requests a
        # webpage, it sends this IP address along with it.
        #
        # https://goo.gl/txEmRd
        self.external_ip_address = None

        # The Media Access Control (MAC) Address is a unique identifier assigned to network
        # interfaces for communications at the data link layer of a network segment. MAC addresses
        # are used as a network address for most IEEE 802 network technologies, including Ethernet
        # and Wi-Fi.
        #
        # https://en.wikipedia.org/wiki/MAC_address
        self.mac_address = None

        # The port number is associated with the IP address of the host and protocol
        # type of communication. A port is identified for each address and protocol by a
        # 16-bit number.
        #
        # https://en.wikipedia.org/wiki/Port_(computer_networking)
        self.ports = None

        # The timestamp when this location was created or updated.
        self.timestamp = None

        # The name to associate with this location.
        self.name = name

    def to_Json(self):
        """to json"""
        pass

    def to_string(self):
        """to string"""
        pass

    def to_location(self, json_obj):
        """convert a json object to a location object"""
        if 'name' in json_obj:
            self.name = json_obj['name']
        if 'ports' in json_obj:
            self.ports = json_obj['ports']
        if 'localIpAddress' in json_obj:
            self.local_ip_address = json_obj['localIpAddress']
        if 'externalIpAddress' in json_obj:
            self.external_ip_address = json_obj['externalIpAddress']
        if 'timestamp' in json_obj:
            self.timestamp = json_obj['timestamp']