import shodan
from config import get_api_key

def query_shodan(ip):
    """
    Queries the Shodan API for the given IP address and returns the result.
    """
    try:
        api_key = get_api_key()
        if not api_key:
            raise ValueError("API key not found. Please set your API key in the configuration.")
        # Initialize the Shodan API
        api = shodan.Shodan(api_key)
        # Query information about the IP address
        result = api.host(ip)
        return result
    except shodan.APIError as e:
        raise Exception(f"Shodan API error: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while querying Shodan: {e}")
