import socket

domain = input("Enter your domain:" )

try:
    ip = socket.gethostbyname(domain)
    print("IP address:", ip)

except socket.gaierror:
    print("DNS resolution failed")