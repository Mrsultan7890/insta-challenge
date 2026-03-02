import urllib.request

public_ip = urllib.request.urlopen("https://ip.ipify.org").read().decode()
print(f"Publi IP: {public_ip}")