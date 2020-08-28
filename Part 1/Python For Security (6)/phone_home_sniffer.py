import socket
from nettypes import EthernetFrame


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    host = "192.168.0.30"
    port = 8085

    forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward.connect((host, port))

    
    while True:
        data, addr = conn.recvfrom(65535)
        
        if data:
            forward.sendall(data)


if __name__ == "__main__":
    main()