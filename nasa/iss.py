#!/usr/bin/python3

import requests
import datetime

# define base URL
URL = "http://api.open-notify.org/iss-now.json"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    iss = requests.get(URL).json()
   # print(iss)
    timestamp = iss["timestamp"]
    date_time = datetime.datetime.fromtimestamp(timestamp) 
    print("\nCurrent location of the ISS:\n " )
    print("Current time is : " , date_time )
    print("\nLatitude: ", iss["iss_position"]["latitude"])
    print("Longitude: ", iss["iss_position"]["longitude"])


if __name__ == "__main__":
    main()

