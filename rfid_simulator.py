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
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
