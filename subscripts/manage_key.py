import os

def new_key(): # Makes a new key
    with open("key.txt", "w") as key:
        key.write(input("Please enter you DonutSMP API key that you can obtain by joining and typing \"/api\".\n   >"))

if os.path.exists("key.txt") == False: # Check if file exists
    new_key # If it doesn't, run new_key

with open("key.txt", "r") as key: # Opens key.txt
    key = key.read() # Set key to the contents of key.txt.