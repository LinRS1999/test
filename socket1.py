import socket

h = '192.168.0.105'
p = 3000
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((h, p))
s1.listen(5)
cs, add = s1.accept()

h = '192.168.0.106'
p = 6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((h, p))
while True:


    ra = cs.recv(512)
    print(type(ra))
    temp = str(ra)
    print(type(temp))
    print(temp)

    s.send(str.encode(temp))

s.close()
cs.close()








