import search
import scraper
import savedata
import datagrapher
import os
 

findgpu = search.FindGPU()
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
    
    while True:    
        rungrapher = input ("See plotted graph of attained data?(y/n)")

        if rungrapher == "y":
            datagrapher.graphItemData()
            exit()

        elif rungrapher == "n":
            exit()



        
def saveAndQuery(data):
    data[1] = [costs.strip("£") for costs in data[1]]
    savedata.itemData(data[2], data[1], data[0])
    return



if __name__ == "__main__":
    searchAndScrape()  
