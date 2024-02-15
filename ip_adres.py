'''

MODUL INI BELUM DI GUNAKAN DI BAGIAN SYSTEM MANAPUN


yang bener


'''

import requests
 
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address

# Call the function to get the IP address
ip = get_ip_address()
print("IP Address:", ip)

import socket as s

ip = s.getfqdn("localhost") 
print(ip)
