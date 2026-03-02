import socket

target = input("Enter target: ")

ports = [80, 443, 21, 22, 8080]

print(f"\n[+] Scanning target {target}\n")

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] {port}")
        else:
            print(f"[CLOSED] {port}")

        s.close()

    except socket.gaierror:
        print("[-] DNS Resolution Failed.")
        break

    except Exception as e:
        print("[-] Error:", e)
        break