import socket

s = socket.socket()
s.bind(("127.0.0.1",1234))

s.listen(5)

conn, addr = s.accept()  #server is waiting for connetions. 


print(conn.getpeername())
data = conn.recv(1024)
print(data.decode())

conn.send(input("enter something for client..").encode("utf-8"))

