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


# def convert_mask(mask):
#     parts = mask.split('.') #['255', '255', '255', '0']
#     mask = 0
#     for octet in parts:
#         mask += bin(int(octet)).count('1')
#
#     return mask
#
#
# def convert_mask2(mask):
#     return sum([bin(int(octet)).count('1') for octet in mask.split('.')])


def convert_mask(mask):
    return sum(bin(int(octet)).count('1') for octet in mask.split('.'))


def is_reachable(ip_address):
    arg = '-c'
    if sys.platform.startswith('win'):
        arg = '-n'

    output = subprocess.run(['ping', arg, '1', ip_address], capture_output=True)
    return 'reachable' not in str(output.stdout)


def is_reachable2(ip_address):
    arg = '-c'
    if sys.platform.startswith('win'):
        arg = '-n'
    try:
        output = subprocess.run(['ping', arg, '1', ip_address], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
