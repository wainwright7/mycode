#!/usr/bin/env python3

# collect input from user
hostname = input("What value should we set for hostname? : ")

# use the lower method to test if input value matches
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
    
else:
     print("Hostname does not match.")

# print out to the user
print("Exiting the script")

