# WHOIS Information Tool Documentation

This Python script retrieves WHOIS information for a given domain name. It utilizes the `python-whois` library to fetch various details such as registrar, name servers, creation date, updated date, and more.

## Getting Started

### Installation

Ensure you have Python installed and follow these steps:

```
apt update -y
apt upgrade -y
apt install git -y
git clone https://github.com/Cyber-Programer/website-info/
cd website-info
python main.py
```

### Usage

Run the script from the command line by providing a domain name:

```bash
python whois_info.py -d example.com -a
```

## Help options

```
#++++++++++++++++++#
         ┓   •  ┏  
    ┓┏┏┏┓┣┓  ┓┏┓╋┏┓
    ┗┻┛┗ ┗┛  ┗┛┗┛┗┛
    ┏•   ┓         
    ╋┓┏┓┏┫┏┓┏┓     
    ┛┗┛┗┗┻┗ ┛     
        (2rootv3) 
#++++++++++++++++++#

usage: main.py [-h] -d DOMAIN [-i] [-u] [-c] [-r] [-n] [-e] [-ct] [-con] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain name (example.com)
  -i, --ip              Display IP address only
  -u, --up              Display Updated date only
  -c, --cp              Display Creation date only
  -r, --rg              Display registrar
  -n, --ns              Display Name Servers
  -e, --em              Display emails
  -ct, --city           Display city
  -con, --country       Display country
  -a, --all             Display all information
```
