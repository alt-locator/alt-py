"""Network utils for alternative location tool."""
import json
import netifaces
import requests
import socket


class NetworkUtils(object):
  """Network utils for alternative location tool."""

  def GetWanIP(self):
    """Gets the external ip address or the WAN IP address.

    Returns:
      The ip address as a string.
    """
    r = requests.get('https://api.ipify.org?format=json')
    json_data = json.loads(r.text)
    return json_data['ip']

  def GetLanInterface(self):
    """Gets the LAN IP address.

    Inspired by: http://stackoverflow.com/questions/270745/
    Another option is to use the sockets module: socket.gethostbyname(socket.gethostname())

    Returns:
      A dictionary of network interfaces associated with the mac address and local ip address.
    """
    internal_addresses = {}
    for interface in netifaces.interfaces():
      mac_address = None
      local_address = None
      try:
        mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
      except KeyError:
        pass

      try:
        local_address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
      except KeyError:
        pass

      if local_address and mac_address:
        internal_addresses[interface] = {
          'mac_address': mac_address,
          'local_address': local_address
        }
    return internal_addresses