from bs4 import element
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class GPUsearcher:
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

        
        


GPUsearcher.searchGPU(url = "https://www.ebay.co.uk/", gpu = "RTX 3080")
