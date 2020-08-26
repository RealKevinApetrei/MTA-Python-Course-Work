import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "194.168.4.100"
    port = 53

    result = s.connect_ex((host, port))
    print("Result: {}".format(result))
    s.close()


if __name__ == "__main__":
    main()
