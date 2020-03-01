from selenium import webdriver
import csv
import time
import pickle

url = 'https://hk.carousell.com'
driver = webdriver.Chrome('D:\\honk\\chromedriver.exe')
driver.get(url)
time.sleep(1)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get(url)


file = open('sample.csv', 'r')

for i in file:
    u = i.replace('\n','')
    driver.get(u)
    time.sleep(1)
    elems = driver.find_elements_by_xpath("//img[@src = 'https://mweb-cdn.karousell.com/build/like-outlined-110d8c524ae4580258130ea6f75ef84c.svg']")
    for j in elems:
        j.click()
        time.sleep(1)
