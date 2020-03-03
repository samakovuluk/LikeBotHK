from selenium import webdriver
import csv
import time
import pickle
import random


minV=1
maxV=2
waitingForReload=1
waitingAfteLike=3

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

#Expanding all hided items and we getting target url
def expandAll(u,k,w):
    print("action expand")
    #here the try and exept, because program did not know in which language it will show, and i did it for all language
    try:
        while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), 'View more')]")!=[]:
            cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), 'View more')]")
            cl.click()
            time.sleep(random.randint(minV, maxV))
    except:
        try:
            while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), '瀏覽更多')]")!=[]:
                cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), '瀏覽更多')]")
                cl.click()
                time.sleep(random.randint(minV, maxV))
        except:
            try:
                while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), '睇更多')]")!=[]:
                    cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), '睇更多')]")
                    cl.click()
                    time.sleep(random.randint(minV, maxV))
            except:
                try:
                    while driver.find_elements_by_xpath("//button[@type = 'button'][contains(text(), 'Lihat lebih banyak')]")!=[]:
                        cl = driver.find_element_by_xpath("//button[@type = 'button'][contains(text(), 'Lihat lebih banyak')]")
                        cl.click()
                        time.sleep(random.randint(minV, maxV))
                except:
                    if len(getEmptyFields())<=1:
                        print("Problem in server, and there is no items")
                        #so if program did not find button to expand it will reload again three times and with waiting 10 seconds
                        time.sleep(waitingForReload)
                        driver.get(u)
                        if k<=3:
                            expandAll(u, k+1)
                    else:
                        worker(u,w)

    #if we have empty like fields so we going to find empty like fields and click it them for all
    if len(getEmptyFields())>1:
        worker(u,w)

#here we finding empty like fields by svg.
def getEmptyFields():
    print("action find empty fields")
    return driver.find_elements_by_xpath("//img[@src = 'https://mweb-cdn.karousell.com/build/like-outlined-110d8c524ae4580258130ea6f75ef84c.svg']")

#This for like all empty fields
def worker(u,w):
    print("action like worker")
    elems = getEmptyFields()
    print('Finding empty like fields')
    for j in range(1, len(elems)):
        try:
            elems[j].click()
            print("Like")
            time.sleep(random.randint(minV, maxV))
        except:
            continue
    print("Waiting ",waitingAfteLike)
    time.sleep(waitingAfteLike)

    #here why one, not zero, because we have one empty like field in the navbar, and it is conts field, and for that we did >1
    if len(getEmptyFields())>1:
        #if we will have more than one so we calling method again
        w+=1
        if (w<=3):
            driver.get(u)
            print("Running again ", w)
            expandAll(u,0,w)


def main():
    init()
    file = open('sample.csv', 'r')
    for i in file:
        u = i.replace('\n','')
        print("Store url - ", u )
        driver.get(u)
        time.sleep(2)
        print("Expanding all hided orders")
        expandAll(u,0,0)
    print("Finished")






if __name__ == '__main__':
    main()
