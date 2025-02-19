import sys
from shodan_recon import query_shodan
from Reports.shodan_report import generate_shodan_report
from config import get_api_key, save_api_key, check_api_key
from banner import get_banner

def setup_api_key():
    """
    Ask the user to input their Shodan API key and saves it.
    """
    print("\033[91m" + "[-] Shodan API key not found." + "\033[0m")

    key = input("[+] Enter your Shodan API key: ").strip()
    try:
        save_api_key(key)
        print("\n[+] API key saved successfully!\n")
    except Exception as e:
        print(f"Error saving API key: {e}")
        sys.exit(1)

def main():

    print(get_banner())
    # Ensure the API key is set
    if not check_api_key():
        setup_api_key()

    while True:
        print("1. Extract information from an IP address")
        print("2. Exit\n")
        choice = input("\nSelect an option: \n").strip()

        if choice == "1":
            ip = input("[+] Enter the IP address: ").strip()
            try:
                
                result=query_shodan(ip)
                generate_shodan_report(result)
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == "2":
            print("Exiting DeepRecon. Goodbye!")
            break
        else:
            print("\033[91m" + "[-] Invalid option. Please try again.\n"+ "\033[0m")


if __name__ == "__main__":
    main()

