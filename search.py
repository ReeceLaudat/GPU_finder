from bs4 import element
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


# This searches for the GPU
def searchGPU (url, gpu):
    driver = webdriver.Firefox()
    driver.get(url)
    elementSearchBar = driver.find_element(By.ID, "gh-ac")
    
    elementSearchBar.send_keys(gpu)
    elementSearchBar.send_keys(Keys.ENTER)
    sleep(3)
    elementBIN = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/div[1]/div/div[2]/div[2]/div[1]/div/ul/li[3]/a")
    driver.get(elementBIN.get_attribute("href"))

    
def searchGPUfacebook(url, gpu):
    driver = webdriver.Firefox()
    driver.get(url)
  
    elementDeclineCookie = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/span/span")
    elementDeclineCookie.click()
    elementCloseLogin = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/i") 
    elementCloseLogin.click()

    elementSearchBar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input")

    elementSearchBar.send_keys(gpu)
    elementSearchBar.send_keys(Keys.ENTER)
    sleep(3)

    elementLocationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div/span")
    elementLocationFilter.click()
    
    elementSetLocation = driver.find_element(By.XPATH, "//*[@id=':r37:']")
    elementSetLocation.clear() 
    elementSetLocation.send_keys("London, United Kingdom")
    sleep(2)
    elementSelectLocation = driver.find_element(By.XPATH, "//*[@id=':r3f:']")
    elementSelectLocation.click()
    elementLocationApply = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div[1]/div/span/span")
    elementLocationApply.click()

            

#GPUsearcher.searchGPU(url = "https://www.ebay.co.uk/", gpu = "RTX 3080")
searchGPUfacebook(url = "https://www.facebook.com/marketplace", gpu = "RTX 3080")
