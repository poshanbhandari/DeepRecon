# DeepRecon
```
  ___                  ____                                  
|  _ \  ___  ___ _ __ |  _ \ ___  ___ ___  _ __                                    
| | | |/ _ \/ _ \ '_ \| |_) / _ \/ __/ _ \| '_ \
| |_| |  __/  __/ |_) |  _ <  __/ (_| (_) | | | | 
|____/ \___|\___| .__/|_| \_\___|\___\___/|_| |_|
                |_|                                                                                                                                                                                        
1. Extract information from an IP address
2. Exit
```

DeepRecon is an open-source reconnaissance tool designed to gather and aggregate information from various target types including IP addresses, domains, phone numbers, and more. Currently, the tool implements a Shodan module to fetch detailed information about a given IP address using the Shodan API. Additional features will be implemented in the coming days.

## 🚀 Features  
- [x] **IP Information Extraction**:Gather detailed information about a given IP address using the Shodan API.  

## 🔮 Roadmap (Planned Features)  

- **Domain**: Extract information about the domain of the target. *(Coming Soon)*
- **Phonenumber**: Collect information about a phone number. *(Coming Soon)*
- **Mail Breach**: Check if a given domain has been involved in a mail breach. *(Coming Soon)*
- **DNS Map**: Map DNS records associated with the target. 
- **Mx Lookup**: Gather mail records of the target. *(Coming Soon)*
- **Metadata**: Extract all metadata from a given file. *(Coming Soon)*
- **Honeypot**: Check if a system is a honeypot or a real system. *(Coming Soon)*
- **MAC Address Lookup**: Obtain information about a given MAC address. *(Coming Soon)*
- **Username**: Extract account information from social media using a username. *(Coming Soon)*
- **IP2Proxy**: Check whether an IP address is using a VPN/Proxy service. *(Coming Soon)*



### Prerequisites

- Python 3.7 or higher.
- A [Shodan API Key](https://www.shodan.io/) for the Shodan module.
- Install the required package:

 ```
pip install -r requirements.txt
```

### Installation

Clone the repository:
```
git clone https://github.com/poshanbhandari/deepRecon.git
cd deepRecon
```

### Usage  
```
python deeprecon.py
```



