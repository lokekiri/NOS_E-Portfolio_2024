import socket

def get_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        print(f"The IP address of {website_url} is {ip_address}")
    except socket.gaierror:
        print(f"Unable to get the IP address for {website_url}")

# Example usage
website = input("Enter website URL (without 'https://'): ")
get_ip_address(website)
