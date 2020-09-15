import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = ""

while msg != "exit":
    a = input("Type in your message: ")
    s.sendto(str.encode(a), ("127.0.0.1", 12345))
    recv_msg = s.recvfrom(1024)
    msg = recv_msg[0].decode()
    print("The Message has been received: ", msg)