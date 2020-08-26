from utils import timefunc
from port_scanner import Scanner
from grabber import Grabber


@timefunc
def main():
    ip = "194.168.4.100"
    portrange = (50, 55)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports: 
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("ERROR: {}".format(e))


if __name__ == "__main__":
    main()
