import scrapy

#1 : Identifing target website:
#This spider will scrape quotes from : quotes.toscrape.com

class quotesSpi(scrapy.Spider):
    name = "Spidy"      #Identifies the spider

    #2 : Collecting urls :
    #using start_request class attribute.
    #now this list will be used as default implementation of start_request().

    start_request = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"

    ]
    


    #using start_request() method:
    # Generates Request obj from url
'''
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
    ''
    1.Scrapy schedules the scrapy.Request obj returned by start_request method.
    2.Then after it recives a response, it instantiates response obj.
    3.Now it calls the callback method associated with request, passing the response obj as arg.       \
        
    so Request obj => Response obj => callback to associated method

    #
''' 

    #3. Handling the urls:
    def parse(self, response):          #This method will handle the response downloaded for each request made. Also finding new URLs to follow.
        #This is where we'll parse the scraped data the way we like.    
        page = response.url.split("/")[-2] # response.url : To get url of the response obj as string.
    
        #To extract page number which is the 
        #split the url with "/" as delim, which will split the url into a list , 
        #now take the second item from the end of the list, so we get the page number.



        fileName = f'quotes-{page}.html'    # we'll save it in a html file
        with open(fileName,'wb') as f:      # create and open a file with write and byte passed.
            f.write(response.body) # this will write the response body ..which is in byte form

# To run spider :
# $ scrapy crawl spidy
# From quotesScrape dir


