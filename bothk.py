from selenium import webdriver
import csv
import time
import pickle
import random

#url and driver are our global variable
url = 'https://hk.carousell.com'
driver = webdriver.Chrome('chromedriver.exe')

#here we puuting our cookies file to authorize
def init():
    driver.get(url)
    time.sleep(1)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url)

#Expanding all hided items
def expandAll():
    #here the try and exept, because program did not know in which language it will show, and i did it for all language
    try:
        while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), 'View more')]")!=[]:
            cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), 'View more')]")
            cl.click()
            time.sleep(random.randint(2, 7))
    except:
        try:
            while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), '瀏覽更多')]")!=[]:
                cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), '瀏覽更多')]")
                cl.click()
                time.sleep(random.randint(2, 7))
        except:
            try:
                while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), '睇更多')]")!=[]:
                    cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), '睇更多')]")
                    cl.click()
                    time.sleep(random.randint(2, 7))
            except:
                try:
                    while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), 'Lihat lebih banyak')]")!=[]:
                        cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), 'Lihat lebih banyak')]")
                        cl.click()
                        time.sleep(random.randint(2, 7))
                except:
                    print("Error")

#here we finding empty like fields by svg.
def getEmptyFields():
    return driver.find_elements_by_xpath("//img[@src = 'https://mweb-cdn.karousell.com/build/like-outlined-110d8c524ae4580258130ea6f75ef84c.svg']")

#This is recursion method to call again if we will have empty like after 30 seconds
def worker():
    elems = getEmptyFields()
    print('Finding empty like fields')
    for j in range(1, len(elems)):
        try:
            elems[j].click()
            print("Like")
            time.sleep(random.randint(1, 7))
        except:
            continue
    print("Waiting 30s")
    time.sleep(30)

    #here why one, not zero, because we have one empty like field in the navbar, and it is conts field, and for that we did >1
    if len(getEmptyFields())>1:
        print("Running again")

        #if we will have more than one so we calling method again
        worker()


def main():
    init()
    file = open('sample.csv', 'r')
    for i in file:
        u = i.replace('\n','')
        print("Store url - ", u )
        driver.get(u)
        time.sleep(2)
        print("Expanding all hided orders")
        expandAll()
        worker()
    print("Finished")






if __name__ == '__main__':
    main()
