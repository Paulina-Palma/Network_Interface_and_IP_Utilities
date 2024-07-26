import netifaces
import ipaddress
from network import extract_ip_address, convert_mask, is_reachable, is_reachable2


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


ip = extract_ip_address()
network_interfaces = NetworkInterfaces()
netmask = network_interfaces[ip]['netmask']
netmask_as_number = convert_mask('255.255.255.0')

all_addresses = ipaddress.IPv4Network(f'{ip}/{netmask_as_number}', strict=False)
for address in all_addresses.hosts():
    address = str(address)
    if is_reachable2(address):
        print(address)
