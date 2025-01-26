import requests
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup
import search
import scraper
import os

findgpu = search.findGPU()
scrapeGPU = scraper.GPU_scraper()
def startfunc():
    gpu = input ("What gpu would you like to find? ")
    website = input ("What website? ")
    if website == "ebay":
        gpuData = findgpu.ebay_search(gpu)
        scrapeGPU.scrape_gpus_ebay(gpuData)

    elif website == "facebook":
        gpuData = findgpu.facebook_search(gpu)
        fbmp_page_file = open("product_page.html", "w")
        fbmp_page_file.write(gpuData)
        fbmp_page_file.close()
        fbmpFilePath = os.getcwd() + "/product_page.html" 
        scrapeGPU.scrape_gpus_fbmp(fbmpFilePath)
    
    elif website == "both":
        gpuData = findgpu.search_both(gpu)
        
 
def scraper(url):
   scrape_gpus(url)



if __name__ == "__main__":
    startfunc() 
