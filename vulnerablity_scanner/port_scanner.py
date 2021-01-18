import socket
from IPy import IP


class PortScanner:
    banners = []
    open_port = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                pass
            sock.close()
        except:
            pass

    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan(self):
        print('\n' + '[...Scanning Target] ' + str(self.target))
        for port in range(1, 100):
            self.scan_port(port)
