"""Client to send OSC datagrams to an OSC server via UDP."""

"""3Client IP, Port Version. 21.09.06"""

import socket


class UDPClient_1(object):
  """OSC client to send OscMessages or OscBundles via UDP."""

  def __init__(self, address, port1):
    """Initialize the client.

    As this is UDP it will not actually make any attempt to connect to the
    given server at ip:port until the send() method is called.
    """
    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._sock.setblocking(0)
    self._address = address
    self._port1 = port1

    
  def send(self, content):
    """Sends an OscBundle or OscMessage to the server."""
    self._sock.sendto(content.dgram, (self._address, self._port1))





class UDPClient_2(object):

  def __init__(self, address, port2):

    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._sock.setblocking(0)
    self._address = address
    self._port2 = port2
    
    
  def send(self, content):
    self._sock.sendto(content.dgram, (self._address, self._port2))




class UDPClient_3(object):


  def __init__(self, address, port3):

    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._sock.setblocking(0)
    self._address = address
    self._port3 = port3



  def send(self, content):
    self._sock.sendto(content.dgram, (self._address, self._port3))


class UDPClient_4(object):


  def __init__(self, address, port4):

    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._sock.setblocking(0)
    self._address = address
    self._port4 = port4



  def send(self, content):
    self._sock.sendto(content.dgram, (self._address, self._port4))




class UDPClient_5(object):


  def __init__(self, address, port5):

    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._sock.setblocking(0)
    self._address = address
    self._port5 = port5



  def send(self, content):
    self._sock.sendto(content.dgram, (self._address, self._port5))

