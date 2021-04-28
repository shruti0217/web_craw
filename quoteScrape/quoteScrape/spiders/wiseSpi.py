import scrapy

#1 : Identifing target website:
#This spider will scrape quotes from : quotes.toscrape.com

class quotesSpi(scrapy.Spider):
    name = "Spidy"      #Identifies the spider

    #2 : Collecting urls :

    def start_requests(self):       # method used to specify starting urls and collecting more urls from the given urls 
    # so here we are collecting urls in the url list :                               
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"

        ]    
        #
        for url in urls:  
            yield scrapy.Request(url=url, callback=self.parse) # what does callback = self.parse do ? : it will call parse method with response obj as parameter.
            # scrapy.Request will return  response obj for each url
            # using yield we can return from function without destorying the state of its local variables 
            # so here we're returning requests to the urls given using scrapy.Request
            #When program hits yeild it will suspend the fuction and return the url requests
            #
    def parse(self, response):
        page = response.url.split("/")[-2] #To extract page number which is the 
        fileName = f'quotes-{page}.html'    # we'll save it in a html file
        with open(fileName,'wb') as f:
            f.write(response.body) # this will write the response body ..which is in byte form

# To run spider :
# $ scrapy crawl spidy
# From quotesScrape dir

