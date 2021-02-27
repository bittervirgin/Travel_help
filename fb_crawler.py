from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#Khai bao browser
browser = webdriver.Firefox()

#Open URL
browser.get("https://www.facebook.com/groups/halotravel?sorting_setting=CHRONOLOGICAL")
sleep(5)

#Scroll to have more posts
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#sleep(10)

#Get post
posts_link = browser.find_element_by_xpath("//div[@data-pagelet='GroupFeed']")
print(posts_link)
sleep(5)
post = browser.find_elements_by_xpath("//div[@role='article']")
#print(post)
for posts in post:
    #author = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span/h2/span/div/a/strong/span")
    #print(author)
    content = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/span/span/span[2]/span/a")
    content.click()
    sleep(2)
#posts = browser.find_element_by_xpath("//div")
sleep(5)

browser.close()