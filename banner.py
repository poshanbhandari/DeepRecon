# banner.py

MAGENTA = "\033[95m"
RESET = "\033[0m"


BANNER = fr'''
{MAGENTA}
 ____                  ____                      
|  _ \  ___  ___ _ __ |  _ \ ___  ___ ___  _ __  
| | | |/ _ \/ _ \ '_ \| |_) / _ \/ __/ _ \| '_ \ 
| |_| |  __/  __/ |_) |  _ <  __/ (_| (_) | | | |
|____/ \___|\___| .__/|_| \_\___|\___\___/|_| |_|
                |_|             

{RESET}
'''

def get_banner():
    """Return the banner string."""
    return BANNER
