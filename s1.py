import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 12345))
while 1:
    bytesAddressPair = s.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print("The Message has been received: ", message.decode())

    a = input("Type in your Message Here: ")
    s.sendto(str.encode(a), address)