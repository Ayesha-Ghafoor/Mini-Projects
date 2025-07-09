import socket
import uuid

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    return mac_address

if __name__ == "__main__":
    print("IP Address:", get_ip_address())
    print("MAC Address:", get_mac_address())
