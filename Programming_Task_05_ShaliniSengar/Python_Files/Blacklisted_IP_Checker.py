# Blacklisted IP Checker

# List of blacklisted IP addresses
blacklist = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.1.100",
    "192.168.0.50"
]

# Ask the user to enter an IP address
ip_address = input("Enter an IP Address: ")

# Variable to check whether IP is found
found = False

# Search for the IP address using a loop
for ip in blacklist:
    if ip == ip_address:
        found = True
        break

# Display the result
if found:
    print("IP Found in Blacklist")
else:
    print("IP Not Found")
