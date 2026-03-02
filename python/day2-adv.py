import dns.resolver

domain = input("Enter your domain: ")

record_type = ["A", "MX", "NS", "TXT"]

for record in record_type:
    try:
        answers = dns.resolver.resolve(domain, record)
        print(f"\n{record} records:")
        for rdata in answers:
            print(rdata.to_text())

    except:
        print(f"No {record} records Found")