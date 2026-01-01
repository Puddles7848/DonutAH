import requests
import time
import pandas
from io import StringIO

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)

# Define key functions


with open("subscripts/manage_key.py", "r") as key:
    exec(key.read())


def parse_page(): # Gets page 1 with the option to return a JSON or DICT
    url = "https://api.donutsmp.net/v1/auction/transactions/1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+key
    }
    output = pandas.read_json(StringIO(requests.get(url, headers=headers).text)).drop("status", axis=1) # yay
    return output

print(parse_page())