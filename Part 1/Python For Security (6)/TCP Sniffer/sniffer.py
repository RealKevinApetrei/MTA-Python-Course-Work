import socket
from capture import PCAPFile
from nettypes import EthernetFrame, IPHeader


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    # pcap = PCAPFile("packets.pcap")
    while True:
        raw_data, addr = conn.recvfrom(65535)
        ethframe = EthernetFrame(raw_data)
        print(ethframe)
        if ethframe.protocol == 8:
            ipheader = IPHeader(ethframe.leftover_data)
            print(ipheader)
        # pcap.write(raw_data)
    # pcap.close()


if __name__ == "__main__":
    main()
