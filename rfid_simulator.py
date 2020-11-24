# #!/usr/bin/env python3
#
# import socket
# from time import sleep
#
# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 8888       # Port to listen on (non-privileged ports are > 1023)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     count = 0
#     with conn:
#         print('Connected by', addr)
#         while True:
#             conn.sendall("Said Hello".encode())
#             sleep(10000)
#             count += 1
#             # if count >= 10:
#             #     conn.detach()
#             #     conn.close()
#             #     s.detach()
#             #     s.close()
#             #     break




#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
# import zmq

# context = zmq.Context()
#
# #  Socket to talk to server
# print("Connecting to hello world server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")
#
# #  Do 10 requests, waiting each time for a response
# for request in range(10):
#     print("Sending request %s …" % request)
#     socket.send(b"Hello")
#
#     #  Get the reply.
#     message = socket.recv()
#     print("Received reply %s [ %s ]" % (request, message))
import socket
from typing import cast

import serial
import time
import struct

from zeroconf import Zeroconf, ServiceBrowser, ZeroconfServiceTypes, IPVersion, ServiceStateChange

conexao = serial.Serial() # Configuração da conexão
conexao.port = '/dev/tty.usbmodem14601'
conexao.baudrate = 115200
conexao.setDTR(0)
# conexao.open()

class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))
def on_service_state_change(
    zeroconf: Zeroconf, service_type: str, name: str, state_change: ServiceStateChange
) -> None:
    print("Service %s of type %s state changed: %s" % (name, service_type, state_change))

    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        print("Info from zeroconf.get_service_info: %r" % (info))
        if info:
            addresses = ["%s:%d" % (socket.inet_ntoa(addr), cast(int, info.port)) for addr in info.addresses]
            print("  Addresses: %s" % ", ".join(addresses))
            print("  Weight: %d, priority: %d" % (info.weight, info.priority))
            print("  Server: %s" % (info.server,))
            if info.properties:
                print("  Properties are:")
                for key, value in info.properties.items():
                    print("    %s: %s" % (key, value))
            else:
                print("  No properties")
        else:
            print("  No info")
        print('\n')

def pisca(tempo=0.2):
    while True:
        conexao.write(str.encode('0')) # Escreve 1 no arduino (LED acende)
        conexao.flush()
        hello = conexao.read_all()
        int("", 16)
        if hello:
            hello = struct.unpack('f', hello)[0]
            print(round(hello, 3))
        time.sleep(tempo) # Aguarda n segundos
if __name__ == '__main__': # Executa a função

    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_totemone._udp.local.", listener)
    try:
        services = ['_airplay._tcp.local.', '_appletv-v2._tcp.local.', '_companion-link._tcp.local.', '_home-sharing._tcp.local.',
         '_raop._tcp.local.', '_rfb._tcp.local.', '_sleep-proxy._udp.local.', '_smb._tcp.local.',
         '_touch-able._tcp.local.', '_ssh._tcp.local.']
        ip_version = IPVersion.V6Only

        zeroconf = Zeroconf()

        # services = list(ZeroconfServiceTypes.find(zc=zeroconf))
        browser = ServiceBrowser(zeroconf, services, handlers=[on_service_state_change])

        print('\n'.join(ZeroconfServiceTypes.find()))
        # pisca()

        input("Press enter to exit...\n\n")
    finally:
        zeroconf.close()
