# pip install requests termcolor

import string, requests, random, time
from termcolor import colored

# ----------------- CONFIG ----------------- #

headers = {
    "Authorization": "token" # Your token
    #                ^^^^^^^ DO NOT REMOVE THE ""! ONLY REPLACE --> token
}

userlength = 0 # User length
#            ^ DO NOT ADD ANY "" JUST REPLACE 0 WITH YOUR NUMBER!

includenum = "n" # Include numbers (y/n)
#            ^^^ DO NOT REMOVE THE ""! ONLY REPLACE --> n

numbercheck = 0 # How many usernames to check
#             ^ DO NOT ADD ANY "" JUST REPLACE 0 WITH YOUR NUMBER!

delay = 2 # I do not recommend changing this! (IF YOU GET RATE LIMITED ITS FOR 350 SECONDS!)
#       ^ DO NOT ADD ANY "" JUST REPLACE 2 WITH YOUR NUMBER!

# ----------------- CODE ----------------- #

# Generates a random string of letter
def gen(userlength, includenum):
    if includenum == "y":
        letters = string.ascii_lowercase + string.digits
    elif includenum == "n":
        letters = string.ascii_lowercase
    rand = ''.join(random.choice(letters) for i in range(userlength))
    return rand

# Writes it to a .txt file so it gets saved
def write_file(rand):
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{rand}\n')

url = "https://discord.com/api/v9/users/@me/pomelo-attempt" # URL to post the request

print(colored("""
     _                           __   _    _              _ 
    | |                         / /  | |  | |            | |
  __| |___  ___   __ _  __ _   / /_ _| | _| |_ ___   ___ | |
 / _` / __|/ __| / _` |/ _` | / / _` | |/ / __/ _ \ / _ \| |
| (_| \__ \ (__ | (_| | (_| |/ / (_| |   <| || (_) | (_) | |
 \__,_|___/\___(_)__, |\__, /_/ \__,_|_|\_\\__\___/ \___/|_|
                  __/ | __/ |                               
                 |___/ |___/                                
""", 'blue')) # Big ass credits
print(colored(f"Ready...", 'green')) # Prints the "Ready..." so you know its running
for _ in range(numbercheck):
    time.sleep(2) # Delay so no rate limit
    rand = gen(userlength, includenum) # Generates a random string of letter
    data = {
        "username": rand # Put the random string of text in here
    }
    response = requests.post(url, headers=headers, json=data) # Sends the request
    if response.status_code == 200: # Checks if it dindt get rate limited
        if "true" in response.text: # Checks if its used
            print(colored(f"{rand} is taken!", 'red')) # Prints the text
            write_file(rand) # Writes it to a .txt file
        elif "false" in response.text: # Checks if its used
            print(colored(f"{rand} is available!", 'green')) # Prints the text
    elif response.status_code == 429: # Checks if it dindt get rate limited
        print(colored(f"Error: Too many requests! Switch token!", 'red')) # Prints the text
    else: # Checks if it dindt get rate limited
        print(colored(f"Error: {response.text}", 'red')) # Prints the text
