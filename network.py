import socket
import sys
import subprocess


def extract_ip_address():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('1.1.1.1', 1))
        local_ip, _ = st.getsockname()
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        st.close()

    return local_ip


def convert_mask(mask):
    return sum(bin(int(octet)).count('1') for octet in mask.split('.'))


def is_reachable(ip_address):
    arg = '-c' if not sys.platform.startswith('win') else '-n'
    try:
        output = subprocess.run(['ping', arg, '1', ip_address], capture_output=True)
        # Check both 'unreachable' and 'timed out' to cover more cases
        return 'unreachable' not in str(output.stdout).lower() and 'timed out' not in str(output.stdout).lower()

    except Exception as e:
        print(f"Error pinging {ip_address}: {e}")
        return False


def is_reachable_with_ports(ip_address, port_range=range(21, 1025)):
    for port in port_range:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
            result = socket_obj.connect_ex((ip_address, port))
            socket_obj.close()
            if result == 0:
                return True
        except socket.error as e:
            print(f"Socket error on port {port} for IP {ip_address}: {e}")
        finally:
            socket_obj.close()
    return False


def get_hostname_from_ip(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return "Nie można znaleźć nazwy dla tego adresu IP"

