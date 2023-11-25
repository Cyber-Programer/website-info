import argparse
import socket
try:
    import whois
except ModuleNotFoundError:
    import os
    os.system('pip install python-whois')
    os.system('pip install --upgrade python-whois')
    os.system('pip uninstall whois')
import sys
from time import sleep as s
try:
    from colorama import init, Fore, Style
except:
    import os
    os.system('pip install colorama')


class colors:
    RESET = Style.RESET_ALL
    RED = Fore.RED
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN


def text_animation(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        s(0.01)

logo =f'''
{colors.RED}#++++++++++++++++++#{colors.RESET}
         ┓   •  ┏  
{colors.BLUE}    ┓┏┏┏┓┣┓  ┓┏┓╋┏┓{colors.RESET}
{colors.CYAN}    ┗┻┛┗ ┗┛  ┗┛┗┛┗┛{colors.RESET}
{colors.GREEN}    ┏•   ┓        {colors.RESET} 
{colors.YELLOW}    ╋┓┏┓┏┫┏┓┏┓   {colors.RESET}  
{colors.RED}    ┛┗┛┗┗┻┗ ┛     {colors.RESET}
{colors.BLUE}        (2rootv3) {colors.RESET}
{colors.RED}#++++++++++++++++++#{colors.RESET}

'''  
try:
    text_animation(logo)
except KeyboardInterrupt:
    print('\n\nTool is exit by user\n\n')

passer = argparse.ArgumentParser()

passer.add_argument('-d','--domain' ,help='Domain name (example.com)',type=str,required=True)

args = passer.parse_args()


def web_info(url):

    result = whois.whois(url)
    dom = ''


    ip = socket.gethostbyname(url)
    
    if isinstance(result.name_servers,list):
        name_server = colors.GREEN+'\n'.join(result.name_servers)+colors.RESET
    elif result.name_servers is None or result.name_servers == 'null':
        name_server = colors.RED + 'Not Available' + colors.RESET
    else:
        name_server = colors.GREEN+str(result.name_servers)+colors.RESET

    # status = '\n'.join(result.status)
    if isinstance(result.emails,list):
        emails = '\n'.join(result.emails)
    else:
        emails = str(result.emails)
        
    registrar_info = result.get('registrar')
    if registrar_info is None or registrar_info == 'null':
        registrar_display = colors.RED + 'Not Available' + colors.RESET
    elif isinstance(result.registrar_info,list):
        registrar_display = colors.GREEN+'\n'.join(result.registrar_info)+colors.RESET
    else:
        registrar_display = colors.GREEN +registrar_info +colors.RESET
    
    whois_server_info = result.whois_server
    if whois_server_info is None or whois_server_info == 'null':
        whois_disply = colors.RED + 'Not Available' + colors.RESET
    else:
        whois_disply = colors.GREEN +whois_server_info +colors.RESET
        

    domain_name = result.domain_name
    if domain_name is None or domain_name == 'null':
        domain_display = colors.RED + 'Not Available' + colors.RESET
    else:
        for i in result.domain_name:
            dom += i.lower()
            break
        if isinstance(result.domain_name,list):
            domain_display = ', '.join(result.domain_name)
        else:
            domain_display = colors.GREEN +domain_name +colors.RESET


    referral_url = result.whois_server
    if referral_url is None or referral_url == 'null':
        referral_url_display = colors.RED + 'Not Available' + colors.RESET
    else:
        if isinstance(result.referral_url,list):
            referral_url_display = colors.GREEN +'\n'.join(result.referral_url) + colors.RESET
        referral_url_display = colors.GREEN +referral_url +colors.RESET
        
    updated_date = result.updated_date
    if updated_date is None or updated_date == 'null':
        updated_date_display = colors.RED + 'Not Available' + colors.RESET
    elif isinstance(result.update_date,list):
        updated_date_display = colors.GREEN+'\n'.join(result.update_date)+colors.RESET
    else:
        updated_date_display = colors.GREEN +str(updated_date) +colors.RESET
    
    creation_date = result.creation_date
    if creation_date is None or creation_date == 'null':
        creation_date_display = colors.RED + 'Not Available' + colors.RESET
    else:
        creation_date_display = colors.GREEN +str(creation_date) +colors.RESET
    
    status = result.status
    if status is None or status == 'null':
        status_display = colors.RED + 'Not Available' + colors.RESET
    elif isinstance(result.status,list):
        status_display = colors.GREEN + '\n'.join(result.status)+colors.RESET
    else:
        status_display = colors.GREEN +str(status) +colors.RESET
    
    emails = result.emails
    if emails is None or emails == 'null':
        emails_display = colors.RED + 'Not Available' + colors.RESET
    elif isinstance(result.emails,list):
        emails_display = colors.GREEN+'\n'.join(result.emails)+colors.RESET
    else:
        emails_display = colors.GREEN +str(emails) +colors.RESET
    
    dnssec = result.dnssec
    if dnssec is None or dnssec == 'null':
        dnssec_display = colors.RED + 'Not Available' + colors.RESET
    else:
        dnssec_display = colors.GREEN +str(dnssec) +colors.RESET
    
    name = result.name
    if name is None or name == 'null':
        name_display = colors.RED + 'Not Available' + colors.RESET
    else:
        name_display = colors.GREEN +str(name) +colors.RESET
    
    org = result.org
    if org is None or org == 'null':
        org_display = colors.RED + 'Not Available' + colors.RESET
    else:
        org_display = colors.GREEN +str(org) +colors.RESET
    
    adress = result.adress
    if adress is None or adress == 'null':
        adress_display = colors.RED + 'Not Available' + colors.RESET
    else:
        adress_display = colors.GREEN +str(adress) +colors.RESET
    
    city = result.city
    if city is None or city == 'null':
        city_display = colors.RED + 'Not Available' + colors.RESET
    else:
        city_display = colors.GREEN +str(city) +colors.RESET
        
    state = result.state
    if state is None or state == 'null':
        state_display = colors.RED + 'Not Available' + colors.RESET
    else:
        state_display = colors.GREEN +str(state) +colors.RESET
    
    registrant_postal_code = result.registrant_postal_code
    if registrant_postal_code is None or registrant_postal_code == 'null':
        registrant_postal_code_display = colors.RED + 'Not Available' + colors.RESET
    else:
        registrant_postal_code_display = colors.GREEN +str(registrant_postal_code) +colors.RESET
    
    country = result.country
    if country is None or country == 'null':
        country_display = colors.RED + 'Not Available' + colors.RESET
    else:
        country_display = colors.GREEN +str(country) +colors.RESET
    
    data = f'''
{colors.MAGENTA}Ifo of {dom}:{colors.RESET}
-----------------
{colors.YELLOW}Ip : {ip}{colors.RESET} 

{colors.YELLOW}Domain: {domain_display}{colors.RESET}

{colors.YELLOW}Registrar :{colors.RESET}
-----------
{registrar_display}

{colors.YELLOW}Whois Server:{colors.RESET}
-------------
{whois_disply}

{colors.YELLOW}Referral Url:{colors.RESET}
-------------
{referral_url_display}

{colors.YELLOW}Updated Date:{colors.RESET}
-------------
{updated_date_display}

{colors.YELLOW}Creation Date:{colors.RESET}
--------------
{creation_date_display}

{colors.YELLOW}Name Servers:{colors.RESET}
-------------
{name_server}

{colors.YELLOW}Status:{colors.RESET}
-----------
{status_display}

{colors.YELLOW}Emails:{colors.RESET}
-----------
{emails_display}

{colors.YELLOW}Dnssec:{colors.RESET}
--------
{dnssec_display}

{colors.YELLOW}Name:{colors.RESET}
--------
{name_display}

{colors.YELLOW}Org:{colors.RESET}
----
{org_display}

{colors.YELLOW}Address:{colors.RESET}
---------
{adress_display}

{colors.YELLOW}City:{colors.RESET}
------
{city_display}

{colors.YELLOW}States:{colors.RESET}
--------
{state_display}

{colors.YELLOW}Registrant postal Code:{colors.RESET}
-----------------------
{registrant_postal_code_display}

{colors.YELLOW}Country:{colors.RESET}
--------
{country_display}
    \n'''

    return data


if __name__ == '__main__':
    
    url =  args.domain
    try:
        data = web_info(url)
        text_animation(data)
    except KeyboardInterrupt:
        print('\nTool is stoped by user \n')
