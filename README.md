# WHOIS Information Tool Documentation

This Python script retrieves WHOIS information for a given domain name. It utilizes the `python-whois` library to fetch various details such as registrar, name servers, creation date, updated date, and more.

## Getting Started

### Installation

Ensure you have Python installed and follow these steps:

```
apt update -y
apt upgrade -y
apt install git -y
git clone https://github.com/Cyber-Programer/website-info/edit
cd website-info
python main.py
```

### Usage

Run the script from the command line by providing a domain name:

```bash
python whois_info.py -d example.com
