import operator
import json
import requests
from credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# A python program to search up a song and give you options based on which artists have a song by the given name
# upon choosing which song version you would like, the song lyrics are displayed

uid = uid
token_id = token_id

my_search = input("What song would like you search for: ")
search_parse =str(my_search)
base_url = f"https://www.stands4.com/services/v2/lyrics.php?uid={uid}&tokenid={token_id}&term={search_parse}&format" \
           f"=json "

PATH = "C:/Users/adeko/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(PATH)

response = requests.get(base_url)

response_json = response.json()# Just storing  the JSON object

json.dumps(response_json)#Convert to a JSON String


for t in response_json['result']:  # MAKE SURE YOU ARE Looping through the json object AFTER you have json.dump'd it
    print("-------------------" + "\n" + t['artist'])

selection = input("Which artist would you like lyrics from: ")# User inputs which artist they want
for t in response_json['result']:
    user_inp = selection.lower()
    artist = str(t['artist'])
    if user_inp == artist.lower():# If we find an artist that matches our user input
        driver.get(t['song-link'])# We get the link to the song by that artist
        break

main = driver.find_element_by_class_name('lyric-body.wselect-cnt')# We find the element that contains the lyrics
print(main.text)# Printing the Lyrics

f = open(f"{driver.title}.txt", "a") #Write the lyrics to a text file
f.write(main.text)
f.close()
