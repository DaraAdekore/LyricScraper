import operator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# A python program to search up a song and give you options based on which artists have a song by the given name
# upon choosing which song version you would like, the song lyrics are displayed

PATH = "C:/Users/adeko/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.lyrics.com/")

main = driver.find_element_by_name("st")

main.send_keys(input("What song would you like to search.."))

main.send_keys(Keys.RETURN)

driver.get(driver.current_url)  # need to update the current page document that we're working with.
# main = driver.find_element_by_css_selector('Button.btn.btn-3.btn-xs.primary')  not being used at the moment.
# ^ just used to learn how to use css selector
main = driver.find_element_by_id('content-body')
result_list = main.find_elements_by_css_selector('p.lyric-meta-album-artist')
for results in result_list:
    print(results.text)

selection = input("Which artist would you like...")
result_list2 = main.find_elements_by_xpath('//div[@class="sec-lyric clearfix"]')
for results in result_list2:
    if operator.contains(results.text, selection):
        results.click()
        break

driver.get(driver.current_url)  # need to update the current page document that we're working with.
main = driver.find_element_by_class_name("lyric.clearfix")
lyrics = main.find_element_by_xpath('//pre[@id="lyric-body-text"]')
title = driver.title + ".txt"
f = open(title, "a")
f.write(lyrics.text)
f.close()