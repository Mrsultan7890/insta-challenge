import socket
import time

target = "gdsddfdf.com"

port = 80

try:
    print(f"[+] target: {target}")
    print(f"[+] port: {port}")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    start_time = time.time()
    print("initiating TCP Handshake...")
    s.connect((target, port))

    end_time = time.time()

    print(f"[+] Time taken {round(end_time - start_time, 4)} seconds")
    print("Handshake successful")

    s.close()
except socket.error as e:
    print("Connection Failed", e)