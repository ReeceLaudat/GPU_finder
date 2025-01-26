from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


class GPU_scraper:
    def scrape_gpus_ebay(self, url):
        html_page = urlopen(url).read()
        soup = BeautifulSoup(html_page, 'html.parser')
        item_name = []
        item_cost = []
        item_links = []

        for name, cost, link in zip(soup.find_all("span", role="heading"), soup.find_all("span", class_="s-item__price"), soup.find_all("a", class_="s-item__link")):
            if link.get("href")[-5:] == "BIN=1":
                item_name.append(name.text.strip())
                item_cost.append(cost.text.strip())
                item_links.append(link.get("href"))
        print(item_links)
        print(item_cost)
        print(item_name)

    def scrape_gpus_fbmp(self, url):
        html_page = open(url).read()
        soup = BeautifulSoup(html_page, 'html.parser')
        item_name = []
        item_cost = []
        item_links = []
        

        for name, cost, link in zip(soup.find_all("span", class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6"), soup.find_all("span", class_="x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1tu3fi x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u"), soup.find_all("a", role="link")):
            if link.get("href")[-5:] == "!%3AD":
                item_name.append(name.text.strip())
                item_cost.append(cost.text.strip())
                item_links.append("https://www.facebook.com/" + link.get("href"))
        print(item_links)
        print(item_cost)
        print(item_name)



