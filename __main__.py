import search
import scraper
import savedata
import os
 

findgpu = search.findGPU()
scrapeGPU = scraper.GPU_scraper()
def searchAndScrape():
    gpu = input ("What gpu would you like to find? ")
    website = input ("What website? ")
    if website == "ebay":
        gpuData = findgpu.ebay_search(gpu)
        ebayListings = scrapeGPU.scrape_gpus_ebay(gpuData)

        saveAndQuery(ebayListings)        

    elif website == "facebook":
        gpuData = findgpu.facebook_search(gpu)
        
        fbmp_page_file = open("product_page.html", "w")
        fbmp_page_file.write(gpuData)
        fbmp_page_file.close()
        fbmpFilePath = os.getcwd() + "/product_page.html" 
        
        fbmpListings = scrapeGPU.scrape_gpus_fbmp(fbmpFilePath)

        saveAndQuery(fbmpListings)
    

        
def saveAndQuery(data):
    savedata.itemData(data[2], data[1], data[0])
    return



if __name__ == "__main__":
    searchAndScrape()  
