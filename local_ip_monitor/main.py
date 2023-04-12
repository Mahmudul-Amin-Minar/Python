import subprocess
import ipaddress


def scan_network(network, range_start, range_end):
    """
    Scan a network for live hosts using ICMP echo requests (ping).

    Args:
        network (str): The network address to scan (e.g. '192.168.0.').

    Returns:
        A list of IP addresses that are live on the network.
    """
    local_host = network.split('.')
    network = f"{local_host[0]}.{local_host[1]}.{local_host[2]}."
    live_hosts = []
    for i in range(range_start, range_end+1):
        ip = network + str(i)
        try:
            output = subprocess.check_output(['ping', '-n', '1' '-w' '1000', ip], shell=True)
            output_str = output.decode('utf-8')
            if "Destination host unreachable" in output_str or "Request timed out" in output_str:
                print(f"{ip} is offline")
            else:
                print(f"{ip} is live")
                live_hosts.append(ip)
        except subprocess.CalledProcessError:
            print(f"{ip} is unreachable")
    return live_hosts



def validate_network_address(network_address):
    """
    Check if the given network address is valid.

    Args:
        network_address (str): The network address to validate.

    Returns:
        True if the network address is valid, False otherwise.
    """
    try:
        # Create an IPv4Network object from the network address string
        network = ipaddress.IPv4Network(network_address)
        # Check if the network address is valid
        return True
    except ValueError:
        # If the network address string is invalid, return False
        return False

def main_menu():
    while(True):
        network_address = input("Enter the network address to scan (e.g. '192.168.0.1') or press q to exit: ")

        if network_address == "q":
            break

        if validate_network_address(network_address):
            range_start = int(input("Enter the starting range of host to be scanned (1-255): "))
            range_end = int(input("Enter the end range of host to be scanned: "))
            live_hosts = scan_network(network_address, range_start, range_end)
            print(f"\nLive hosts on {network_address}:")
            for host in live_hosts:
                print(host)
            print("\n\n")
        else:
            print("Given network is not valid")


if __name__ == '__main__':
    main_menu()
