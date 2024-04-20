import socket
import time
import configparser

def get_time(lie_seconds):
    current_time = int(time.time() * 10**9)
    lied_time = current_time + lie_seconds * 10**9
    return lied_time

def main():
    config = configparser.ConfigParser()
    config.read('server.conf')
    lie_seconds = int(config.get('SNTP', 'lie_seconds'))

    server_address = ('localhost', 123)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    while True:
        data, addr = sock.recvfrom(1024)
        lied_time = get_time(lie_seconds)
        lied_time_bytes = lied_time.to_bytes(8, byteorder='big')
        sock.sendto(data[:40] + lied_time_bytes + data[48:], addr)

if __name__ == '__main__':
    main()