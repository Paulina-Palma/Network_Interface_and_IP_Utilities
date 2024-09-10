## Network Interface and IP Utilities

This project comprises a set of Python utilities and classes designed to facilitate network interface and IP address management. It provides functionalities to retrieve network information, determine network reachability, and resolve hostnames, which are essential for network diagnostics and monitoring.

#### Key Components:

1.  **NetworkInterfaces Class**:
    
    -   **Purpose**: To gather and store network interface details using the  `netifaces`  library.
    -   **Functionality**:
        -   It retrieves all available network interfaces and their associated address information, including IP addresses and netmasks.
        -   Allows access to this data via dictionary-like key indexing.
        
2.  **Utility Functions**:
    
    -   **extract_ip_address()**: Determines the primary IP address of the system by attempting a connection to an external IP, which helps identify the default outbound interface.
    -   **convert_mask(mask)**: Converts a subnet mask (e.g.,  `255.255.255.0`) into the number of bits used in CIDR notation.
    -   **is_reachable(ip_address)**: Uses the  `ping`  command to check if a given IP address is reachable, accommodating platform differences (Unix-like vs. Windows systems).
    -   **is_reachable_with_ports(ip_address, port_range)**: Checks if any specified ports on an IP address are open, useful for determining if a host is accessible and potentially what services are available.
    -   **get_hostname_from_ip(ip_address)**: Resolves an IP address to a hostname, aiding in network diagnostics by providing human-readable identifiers for devices.

#### Implementation Details:

-   **Error Handling**: The utility functions include error handling to manage exceptions, such as unreachable IPs or failed hostname resolutions, ensuring robustness and preventing crashes.
-   **Performance Considerations**: The range of ports checked by  `is_reachable_with_ports`  is configurable, allowing the script to focus on common ports to improve performance.
-   **Platform Compatibility**: The functions are designed to work across different operating systems, with specific handling for commands like  `ping`.

### Use Cases:

This project is particularly useful in network administration and diagnostics, allowing users to:

-   Identify and enumerate network interfaces and their properties.
-   Determine the reachability of network hosts.
-   Resolve hostnames from IP addresses for easier identification of devices on the network.
-   Check for open ports on networked devices, which can indicate the availability of specific services.

Overall, the project provides a comprehensive toolkit for network monitoring and troubleshooting, with a focus on efficiency, flexibility, and ease of use.
