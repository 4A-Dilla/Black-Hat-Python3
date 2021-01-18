import socket
from IPy import IP


def get_banner(soc):
    return soc.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1.0)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode()))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[...Scanning Target] ' + str(target))
    for port in range(1, 65535):
        scan_port(converted_ip, port)


if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan(split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
