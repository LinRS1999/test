import socket

h = '192.168.0.106'
p = 6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((h, p))
while True:

    temp = input()
    s.send(str.encode(temp))
    res = s.recv(512)
    print(res)
s.close()







