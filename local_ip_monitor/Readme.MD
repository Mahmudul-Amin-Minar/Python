# Network Scanner

This is a Python script for scanning a network for live hosts using ICMP echo requests (ping). It allows the user to enter a network address, starting and ending range of hosts to be scanned. The script then pings each host in the specified range and returns a list of IP addresses that are live on the network.

## Dependencies
- Python 3.x

## How to Use

1. Clone or download this repository to your local machine.
2. Open the terminal or command prompt.
3. Navigate to the directory containing the downloaded files.
4. Run the script using the following command:
5. Enter the network address to be scanned in the format `192.168.0.` (replace `192.168.0` with the appropriate network address).
6. Enter the starting and ending range of hosts to be scanned.
7. The script will then ping each host in the specified range and return a list of IP addresses that are live on the network.

## Functions

### scan_network(network, range_start, range_end)

This function scans a network for live hosts using ICMP echo requests (ping). It takes the following arguments:

- `network`: The network address to scan (e.g. '192.168.0.').
- `range_start`: The starting range of host to be scanned (1-255).
- `range_end`: The end range of host to be scanned.

The function returns a list of IP addresses that are live on the network.

### validate_network_address(network_address)

This function checks if the given network address is valid. It takes the following argument:

- `network_address`: The network address to validate.

The function returns `True` if the network address is valid and `False` otherwise.

### main_menu()

This function is the main menu of the script. It prompts the user to enter a network address to be scanned, starting and ending range of hosts to be scanned. It then calls the `scan_network()` function and prints a list of live hosts on the network. The function exits when the user enters `q`.

## Contributing

If you find any issues or have any suggestions for improving this script, please feel free to create a pull request or issue.
