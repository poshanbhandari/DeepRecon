import json
import os

CONFIG_FILE = "config.json"

def get_api_key():
    """
    Reads and returns the Shodan API key from the config file.
    Returns None if the file doesn't exist or if the key is not set.
    """
    if not os.path.exists(CONFIG_FILE):
        return None
    try:
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return data.get("api_key")
    except Exception as e:
        raise Exception(f"Error reading API key: {e}")

def save_api_key(api_key):
    """
    Saves the provided Shodan API key into the config file.
    """
    try:
        data = {"api_key": api_key}
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f)
    except Exception as e:
        raise Exception(f"Error saving API key: {e}")

def check_api_key():
    """
    Checks if the API key is set.
    """
    return os.path.exists(CONFIG_FILE) and get_api_key() is not None
