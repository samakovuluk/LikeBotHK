from selenium import webdriver
import csv
import time
import pickle
import random

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
    try:
        while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), 'View more')]")!=[]:
            cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), 'View more')]")
            cl.click()
            time.sleep(random.randint(2, 7))
    except:
        continue
    
    try:
        while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), '瀏覽更多')]")!=[]:
            cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), '瀏覽更多')]")
            cl.click()
            time.sleep(random.randint(2, 7))
    except:
        continue
    
    try:
        while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), '睇更多')]")!=[]:
            cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), '睇更多')]")
            cl.click()
            time.sleep(random.randint(2, 7))
    except:
        continue
    
    try:
        while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), 'Lihat lebih banyak')]")!=[]:
            cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), 'Lihat lebih banyak')]")
            cl.click()
            time.sleep(random.randint(2, 7))
    except:
        continue
    
    elems = driver.find_elements_by_xpath("//img[@src = 'https://mweb-cdn.karousell.com/build/like-outlined-110d8c524ae4580258130ea6f75ef84c.svg']")
    for j in range(1, len(elems)):
        try:
            elems[j].click()
            time.sleep(random.randint(1, 7))
        except:
            continue








        
