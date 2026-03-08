import  ipaddress

net_addr = "8.8.8.8/32"

try:
    network = ipaddress.ip_network(net_addr)
    print(f"Network: {network}")
    print(f"NetMask: {network.netmask}")
    print(f"Host: {network.num_addresses}")
    print(f"Private IP: {network.is_private}")

    if network.is_private:
        print(f"{network } is private")
    else:
        print(f"{network} is public")

    print(f"Network ID: {network.network_address}")
    print(f"Broadcast address: {network.broadcast_address}")

    first, last = list(network.hosts())[0], list(network.hosts())[-1]

    print(f"UsableIP range is {first} to {last}")

except ValueError:
    print(f"{network}  ICDR format is invalid!")