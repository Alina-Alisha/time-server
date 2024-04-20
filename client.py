import socket
import time

def get_time_from_server(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b'\x1b' * 48, server_address)
    data, addr = sock.recvfrom(1024)

    timestamp = int.from_bytes(data[40:48], byteorder='big')

    server_time = timestamp / 10**9
    return server_time

def main():
    server_address = ('localhost', 123)
    server_time = get_time_from_server(server_address)
    print(time.ctime(server_time))

if __name__ == '__main__':
    main()