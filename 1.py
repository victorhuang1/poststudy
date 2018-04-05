# _*_ coding:utf-8 _*_

from selenium import webdriver
import time

browserPath = '/opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage = 'http://www.xxx.cn'

def login(uername,pwd):
    driver = webdriver.PhantomJS(executable_path=browserPath)
    driver.get(homePage)

    urn = driver.find_element_by_name("myID")
    urn.send_keys(uername)
    time.sleep(3) 

    pwd = driver.find_element_by_name("myPW")
    pwd.send_keys(pwd)
    time.sleep(2)

    
    

    
 
