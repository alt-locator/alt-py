class Location:
    '''
    The location model that includes network information.
    '''

    def __init__(self, name = None):
      '''
      The Local (Internal) IP Address. If your computer is connected to a router with default
      settings, that router will automatically assign a local IP address to your computer. Your
      local IP address is hidden from the outside world and used only inside your private network.
      
      https://www.h3xed.com/web-and-internet/whats-the-difference-between-external-and-local-ip-addresses
      '''
      self.localIpAddress = None

      '''
      The External (Public) IP Address. The Internet Service Provider (ISP) assigns you an external
      IP address when you connect to the Internet. When your browser requests a webpage, it sends this
      IP address along with it.
      
      https://www.h3xed.com/web-and-internet/whats-the-difference-between-external-and-local-ip-addresses
      '''
      self.externalIpAddress = None

      '''
      The Media Access Control (MAC) Address is a unique identifier assigned to network interfaces
      for communications at the data link layer of a network segment. MAC addresses are used as a
      network address for most IEEE 802 network technologies, including Ethernet and Wi-Fi.
    
      https://en.wikipedia.org/wiki/MAC_address
      '''
      self.macAddress = None

      '''
      The port number is associated with the IP address of the host and protocol
      type of communication. A port is identified for each address and protocol by a
      16-bit number.
    
      https://en.wikipedia.org/wiki/Port_(computer_networking)
      '''
      self.ports = None

      '''
      The timestamp when this location was created or updated.
      '''
      self.timestamp = None

      '''
      The name to associate with this location.
      '''
      self.name = name
