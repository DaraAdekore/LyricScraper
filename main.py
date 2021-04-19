from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# A python program to search up a song and give you options based on which artists have a song by the given name
# upon choosing which song version you would like, the song lyrics are displayed.

PATH = "C:/Users/adeko/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://genius.com/")

main = driver.find_element_by_name("q")
print("What song would you like to search..")
print("\n")
main.send_keys(input())

main.send_keys(Keys.RETURN)

driver.get(driver.current_url)  # need to update the current page document that we're working with.
main = driver.find_element_by_xpath('/html/body/routable-page/ng-outlet/search-results-page/div/div[2]/div[1]/div['
                                    '2]/search-result-section/div')
cards = main.find_elements_by_class_name('mini_card-info')
for elemnts in cards:
    print("---------------------------------")
    print(elemnts.text)

selection = input("which version would you like?")
for elemnts in cards:

    if selection in elemnts.text:
        elemnts.click()
        break

driver.get(driver.current_url)  # need to update the current page document that we're working with.
main = driver.find_element_by_xpath('/html/body/routable-page/ng-outlet/song-page/div/div/div[2]/div['
                                    '1]/div/defer-compile[1]/lyrics/div/div/section/p')
print(main.text)