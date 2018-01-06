"""The location object."""
import json

import config
import network_utils


class Location(object):
  """The location model that includes network information."""

  def __init__(self, name=None):
    """Creates the location.

    Args:
      name: (string) Location name of the this machine.
    """
    # The name to associate with this location.
    self.name = name

    # The Local (Internal) IP Address. If your computer is connected to a
    # router with default settings, that router will automatically assign a
    # local IP address to your computer. Your local IP address is hidden
    # from the outside world and used only inside your private network.
    #
    # https://goo.gl/txEmRd
    #
    # The Media Access Control (MAC) Address is a unique identifier
    # assigned to network interfaces for communications at the data link
    # layer of a network segment. MAC addresses are used as a network
    # address for most IEEE 802 network technologies, including Ethernet
    # and Wi-Fi.
    #
    # https://en.wikipedia.org/wiki/MAC_address
    self.local_ip_address = None

    # The External (Public) IP Address. The Internet Service Provider (ISP)
    # assigns you an external IP address when you connect to the Internet.
    # When your browser requests a webpage, it sends this IP address
    # along with it.
    #
    # https://goo.gl/txEmRd
    self.external_ip_address = None

  def ToJson(self):
    """Convert this object to json.
    
    Returns:
      A json representation of this object.
    """
    return json.loads(json.dumps(self.__dict__))

  def ToString(self):
    """Convert this object to string.
    
    Returns:
      A string representation of this object.
    """
    location_values = []
    if self.name:
      location_values.append('%s:' % self.name)
    if self.external_ip_address:
      location_values.append('  external ip address: %s' % self.external_ip_address)
    if self.local_ip_address:
      location_values.append('  local ip address:')
      local_ips = json.loads(json.dumps(self.local_ip_address))
      
      for interface in local_ips.keys():
        location_values.append('    %s inet: %s' % (interface, local_ips[interface]['local_address']))
        location_values.append('    %s  mac: %s' % (interface, local_ips[interface]['mac_address']))
    return '\n'.join(location_values)

  def ToLocation(self, json_object):
    """Converts this json object to a location object.

    Args:
      json_object: (json) A json object.
  
    Returns:
      A location object.
    """
    if 'name' in json_object:
      self.name = json_object['name']
    if 'external_ip_address' in json_object:
      self.external_ip_address = json_object['external_ip_address']
    if 'local_ip_address' in json_object:
      self.local_ip_address = json_object['local_ip_address']
    if 'mac_address' in json_object:
      self.mac_address = json_object['mac_address']
    return self
