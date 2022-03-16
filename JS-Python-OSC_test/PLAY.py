
import argparse
from asyncio import protocols
import osc_message_builder
import udp_client

hostIP_1 = "192.168.0.39"
port1 = 8000

class Play:

    # Class 변수 client_1을 정의 하기 위해서 사용
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default= hostIP_1,
                        help="The ip of the OSC server")
    parser.add_argument("--port1", type=int, default=port1,
                        help="The port the OSC server is listening on")

    args = parser.parse_args()
    client_1 = udp_client.UDPClient_1(args.ip, args.port1)


    print("Play_class_test")
    def play(self):
        print("play test1")
        msg = osc_message_builder.OscMessageBuilder(address ="/stop" )
        self.sendOSCdata(msg)

    def sendOSCdata(self, msg):
        msg = msg.build()
        self.client_1.send(msg)