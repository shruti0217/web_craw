import scrapy

#This spider will scrape quotes from : quotes.toscrape.com

class quotesSpi(scrapy.Spider):
    name = "Spidy"      #Identifies the spider

    def start_requests(self):       # method used to specify starting urls and collecting more urls from the given urls 
    # so here we are collecting urls in the url list :                               
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/"

        ]    
        #
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        fileName = f'quotes-{page}.html'
        with open(fileName,'wb') as f:
            f.write(response.body)

# To run spider :
# $ scrapy crawl spidy
