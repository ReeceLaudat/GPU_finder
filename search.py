import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class findGPU:
    # This searches for the GPU
    def ebay_search(self, gpu):
        driver = webdriver.Firefox()
        driver.get("https://www.ebay.co.uk/")
        elementSearchBar = driver.find_element(By.ID, "gh-ac")
        
        elementSearchBar.send_keys(gpu)
        elementSearchBar.send_keys(Keys.ENTER)
        sleep(3)

        try:
            elementItemsPerPageButtonn = driver.find_element(By.XPATH, "//*[@id='gdpr-banner-decline']") 
            elementItemsPerPageButtonn.click()
        except:
            pass

        sleep(2)

        try:

            element240fromdropdown = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li[64]/div[2]/div[2]/span[2]/span/ul/li[2]/a")
            driver.get(element240fromdropdown.get_attribute("href"))
        
        except:
            sleep(3)
            element240fromdropdown = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/div[3]/div[1]/div[3]/ul/li[64]/div[2]/div[2]/span[2]/span/ul/li[2]/a")
            driver.get(element240fromdropdown.get_attribute("href"))
        

        elementBIN = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/div[1]/div/div[2]/div[2]/div[1]/div/ul/li[3]/a")
        driver.get(elementBIN.get_attribute("href"))
        return driver.current_url



    def facebook_search(self, gpu):
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com/marketplace")
      
        elementDeclineCookie = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/span/span")
        elementDeclineCookie.click()
        elementCloseLogin = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/i") 
        elementCloseLogin.click()

        elementLocationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[4]/div[2]/div[1]/div[1]/div/span")
        elementLocationFilter.click()
        sleep(1)
        elementSetLocation = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/label/div[2]/input[1]")
        elementSetLocation.clear() 
        elementSetLocation.send_keys("London, United Kingdom")
        sleep(2)
        elementSelectLocation = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/div/div/div/div/div/div/div/div/div[1]/span[1]")
        
        elementSelectLocation.click()
        elementLocationApply = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div/div/div/div[1]/div/span/span")
        elementLocationApply.click()

        elementSearchBar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input")

        elementSearchBar.send_keys(gpu)
        elementSearchBar.send_keys(Keys.ENTER)
        sleep(2)



        return driver.page_source


    def search_both(gpu):
        ebay_search(gpu)
        facebook_search(gpu)



