import netifaces
import ipaddress
from network import extract_ip_address, convert_mask, is_reachable_with_ports, get_hostname_from_ip


class NetworkInterfaces:
    def __init__(self):
        interfaces = netifaces.interfaces()
        self._inter = self._read_all_interfaces(interfaces)

    @staticmethod
    def _read_all_interfaces(interfaces):
        data = {}
        for interface in interfaces:
            families = netifaces.ifaddresses(interface)
            for number, family in families.items():
                for item in family:
                    data[item['addr']] = item
        return data

    def __getitem__(self, key):
        return self._inter[key]


# Extract the primary IP address of the machine
ip = extract_ip_address()
network_interfaces = NetworkInterfaces()

# Retrieve the corresponding netmask from the network interfaces
netmask = network_interfaces[ip]['netmask']
netmask_as_number = convert_mask(netmask)

# Calculate all possible host addresses within the network
all_addresses = ipaddress.IPv4Network(f'{ip}/{netmask_as_number}', strict=False)
# Iterate over all possible host addresses
for address in all_addresses.hosts():
    address_str = str(address)

    # Get the hostname for the current address
    hostname = get_hostname_from_ip(address_str)

    # Check if the current address is reachable with any open ports
    if is_reachable_with_ports(address_str):
        print(f"Nazwa hosta dla adresu IP {address_str}: {hostname}")

# # ip_address = '192.168.0.13'  # Tutaj podaj interesujący Cię adres IP
# hostname = get_hostname_from_ip(ip_address)
# print(f"Nazwa hosta dla adresu IP {ip_address}: {hostname}")
