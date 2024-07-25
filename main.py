from network import extract_ip_address
import netifaces


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


ip = extract_ip_address() # '192.168.1.1'
network_interfaces = NetworkInterfaces()
print(network_interfaces[ip])
