
from scapy.all import IP, ICMP, sr1

def ping_sweep(network_prefix):
    print(f"[+] Starting ping on {network_prefix}.0/24")

    for i in range(1, 24):
        ip = f"{network_prefix}.{i}"

        packet = IP(dst=ip)/ ICMP()

        response = sr1(packet, timeout=0.1, verbose=False)

        if response:
            print(f"{ip} is UP/Alive")

ping_sweep("192.168.91")