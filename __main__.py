import requests
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup
import search

findgpu = search.findGPU()
def startfunc():
    gpu = input ("What gpu would you like to find? ")
    website = input ("What website? ")
    if website == "ebay":
        findgpu.ebay_search(gpu)
    elif website == "facebook":
        findgpu.facebook_search(gpu)




if __name__ == "__main__":
    startfunc()
