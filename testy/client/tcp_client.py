import socket


def client():
    #host = '127.0.0.1'
    host='192.168.1.101'
    port = 5000

    s = socket.socket()
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
