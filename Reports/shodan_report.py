# Reports/shodan_report.py

def generate_shodan_report(result):
    """
    Parses the Shodan API result and prints a detailed report.
    """
    # Print header information
    print("\n\n===== Shodan Report =====\n\n")
    print(f"[+] Organization: {result.get('org', 'N/A')}")
    print(f"[+] Operating System: {result.get('os', 'N/A')}")
    ports = result.get('ports', [])
    print(f"[+] Open Ports: {', '.join(map(str, ports)) if ports else 'N/A'}")
    hostnames = result.get('hostnames', [])
    print(f"[+] Hostnames: {', '.join(hostnames) if hostnames else 'N/A'}")
    print("=========================\n")

    # Print details of each service found
    services = result.get("data", [])
    if services:
        print("\n\n----- Service Details -----\n\n")
        for service in services:
            print("-" * 40)
            print(f"[+] Port: {service.get('port', 'N/A')}")
            print(f"[+] Service/Product: {service.get('product', 'N/A')}")
            print("\n\n")
            #print("Banner:")
            #print(service.get('data', 'N/A'))
            #print(f"Timestamp: {service.get('timestamp', 'N/A')}")
        print("-" * 40)
    else:
        print("No service data available.")
