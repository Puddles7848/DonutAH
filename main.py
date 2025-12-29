import os
import requests
import json
import pprint
from typing import Optional


# Define key functions


def new_key(): # Makes a new key
    with open("key.txt", "w") as key:
        key.write(input("Please enter you DonutSMP API key that you can obtain by joining and typing \"/api\".\n   >"))


def get_page(type: Optional[str] = None): # Gets page 1 with the option to return a JSON or DICT
    url = "https://api.donutsmp.net/v1/auction/transactions/1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+key
    }
    return json.loads(requests.get(url, headers=headers).text) # yay


if os.path.exists("key.txt") == False: # Check if file exists
    new_key # If it doesn't, run new_key

with open("key.txt", "r") as key: # Opens key.txt
    key = key.read() # Set key to the contents of key.txt.