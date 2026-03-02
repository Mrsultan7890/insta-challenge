import socket

domain = input("enter your domain: ")

try:
    ip = socket.gethostbyname(domain)
    print(f"[+] IP address of {domain} is {ip}")

except socket.gaierror as e:
    print(" dns resolution failed")


   