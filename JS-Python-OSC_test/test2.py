
import argparse
from asyncio import protocols
from cgi import test
import sys
from typing import Text
from typing_extensions import Self
from xml.etree.ElementTree import tostring
import osc_message
import osc_message_builder
import udp_client



hostIP_1 = "192.168.0.39"
port1 = 8000

hostIP_2 = "192.168.0.0"
port2 = 0000

hostIP_3 = "192.168.0.0"
port3 = 0000

hostIP_4 = "192.168.0.0"
port4 = 0000

hostIP_5 = "192.168.0.0"
port5 = 0000

print("test start")


def initOscClient_1(self):
    print(hostIP_1, port1)
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default= hostIP_1,
                        help="The ip of the OSC server")
    parser.add_argument("--port1", type=int, default=port1,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()
    self.client_1 = udp_client.UDPClient_1(args.ip, args.port1)



def initOscClient_2(self):

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default= hostIP_2,
                        help="The ip of the OSC server")
    parser.add_argument("--port2", type=int, default=port2,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()
    self.client_2 = udp_client.UDPClient_2(args.ip, args.port2)


def initOscClient_3(self):

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default= hostIP_3,
                        help="The ip of the OSC server")
    parser.add_argument("--port3", type=int, default=port3,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()
    self.client_3 = udp_client.UDPClient_3(args.ip, args.port3)


def initOscClient_4(self):

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default= hostIP_4,
                        help="The ip of the OSC server")
    parser.add_argument("--port4", type=int, default=port4,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()
    self.client_4 = udp_client.UDPClient_4(args.ip, args.port4)


def initOscClient_5(self):

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default= hostIP_5,
                        help="The ip of the OSC server")
    parser.add_argument("--port5", type=int, default=port5,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()
    self.client_5 = udp_client.UDPClient_5(args.ip, args.port5)

def Play(self):
    print("play test1")
    msg = osc_message_builder.OscMessageBuilder(address ="/play" )
    self.sendOSCdata(msg)
            

def Stop(self):
    msg = osc_message_builder.OscMessageBuilder(address ="/stop" ) 
    self.sendOSCdata(msg)

def Return(self):
    msg = osc_message_builder.OscMessageBuilder(address = "/marker/1" )
    self.sendOSCdata(msg)

def sendOSCdata(self, msg):
    print("test send OSCdata")
    msg = msg.build()
    self.client_1.send(msg)
    self.client_2.send(msg)
    self.client_3.send(msg)
    self.client_4.send(msg)
    self.client_5.send(msg)
    
test_play = Play()

print(test_play)
