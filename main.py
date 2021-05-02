import operator
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# A python program to search up a song and give you options based on which artists have a song by the given name
# upon choosing which song version you would like, the song lyrics are displayed

uid = "8824"
token_id = "1coYz1QadIuDaIU2"
base_url = f"https://www.stands4.com/services/v2/lyrics.php?uid={uid}&tokenid={token_id}&term=forever%20young&artist=Alphaville&format=json"

PATH = "C:/Users/adeko/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(PATH)

response = requests.get(base_url)

response_json = response.json()

json.dumps(response_json)


for t in response_json['result']:  # MAKE SURE YOU ARE Looping through the json object AFTER you have json.dump'd it
    print(t['artist'])
selection = input("Which artist would you like lyrics from: ")
for t in response_json['result']:
    user_inp = selection.lower()
    artist = str(t['artist'])
    if user_inp == artist.lower():
        driver.get(t['song-link'])
        break


"""f = open(f"demofile2.json", "a")
f.write()
f.close()"""
