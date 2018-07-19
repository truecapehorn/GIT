import socket


def server():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()

    print("Polaczenie z: ", str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("od uzytkownika odebrano: "+str(data, 'utf-8'))
        data = str(data, 'utf-8').upper()
        print(" wysylanie: "+str(data))
        c.send(data.encode("utf8"))
    c.close()


if __name__ == "__main__":
    server()
