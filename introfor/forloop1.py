#!/usr/bin/python3
""" Alta3 | Jay
    Working with Basic for loops """

def main():

    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

    approved_vendors = ["cisco", "juniper", "big_ip"]

    for x in vendors:
        print("\nThe vendor is " + x, end="")
        if x not in approved_vendors:
            print(" - NOT AN APRROVED VENDOR!", end="")

    print("\nOut loop has ended.")

main()
