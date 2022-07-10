from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('D:\Projects\scraps\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
query = 'https://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p=1&f=S&l=50&Query=LREP%2F%22Harrity+%26+Harrity%2C+LLP%22&d=PTXT'

driver.get(query)
time.sleep(3) # Let the user actually see something!
html = driver.page_source
soup = bs(html, "html.parser")
l = soup.find_all('tr')
with open('out.txt', 'w') as f:
    for i in l:
        f.write(i.prettify())
        f.write('\n')
f.close()
driver.quit()