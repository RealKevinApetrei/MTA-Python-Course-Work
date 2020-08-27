import socket
from capture import PCAPFile


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    pcap = PCAPFile("packets.pcap")
    while True:
        raw_data, addr = conn.recvfrom(65535)
        pcap.write(raw_data)
    pcap.close()


if __name__ == "__main__":
    main()
