import os
import platform
import sys

print("=== System Information ===\n")

# Operating System Name
print("Operating System Name:", platform.system())

# Current Username
print("Current Username:", os.getlogin())

# Current Working Directory
print("Current Working Directory:", os.getcwd())

# Python Version
print("Python Version:", sys.version)
