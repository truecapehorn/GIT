import socket
from socket import socket, AF_INET, SOCK_DGRAM



def client():
    host='192.168.1.101'
    port = 5000

    s = socket( AF_INET, SOCK_DGRAM )
    s.connect((host, port))

    message = input(">> ")
    while message != 'q':
        s.send(message.encode("utf8"))
        data = s.recv(1024)
        print("Odebrano z serwera: "+str(data, 'utf-8'))
        message = input(">> ")
    s.close()


if __name__ == "__main__":
    client()
