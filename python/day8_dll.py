import subprocess

interface = "eth0"

new_mac = "00:11:22:33:44:66"

print(f"[+] Changing your MAC address for {interface} to {new_mac}")

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])

print("[+] MAC address updated succesfully")