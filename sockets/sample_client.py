import socket

send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



send_sock.connect(("127.0.0.1", 1234))

send_sock.send(input("enter your message").encode("utf-8"))


print(send_sock.recv(1024).decode())
