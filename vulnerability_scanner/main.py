import port_scanner

targets_ip = input('[+] * Enter target to scan for open ports: ')
port_number = int(input('[+] * Enter amount of ports you\'d like to scan: ') or 100)
vulnerable_file = input('[+] * Enter path to the file with vulnerable software: ') or 'banner.txt'
print('\n')

target = port_scanner.PortScanner(targets_ip, port_number)
target.scan()

with open(vulnerable_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('Vulnerability: ' + banner + ' on port ' + str(target.open_port[count]))
        count += 1