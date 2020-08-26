import socket
from utils import timefunc


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return "Scanner: {}".format(self.ip)

    def add_port(self, port):
        self.open_ports.append(port)

    @timefunc
    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port, upperport):
                self.add_port(port)

    def is_open(self, port, upperport):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((self.ip, port))
            print("{}/{}      Result: {}".format(port, upperport, result))
            return result == 0

    def write(self, filepath):
        openport = map(str, self.open_ports)
        with open(filepath, "w") as f:
            f.write("\n".join(openport))


def main():
    ip = "194.168.4.100"
    scanner = Scanner(ip)
    scanner.scan(1, 100)
    scanner.write("./open_ports")


if __name__ == "__main__":
    main()
