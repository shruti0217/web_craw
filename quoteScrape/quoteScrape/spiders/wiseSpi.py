import scrapy

#1 : Identifing target website:
#This spider will scrape quotes from : quotes.toscrape.com

class quotesSpi(scrapy.Spider):
    name = "Spidy"      #Identifies the spider

    #2 : Collecting urls :
    #using start_request class attribute.
    #now this list will be used as default implementation of start_request().
    #To generate initial request.
    #Scrapy will call parse method for each urls.
    #coz parse is default callback method .
    
    start_request = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"

    ]
    

    '''
    #using start_request() method:
    # Generates Request obj from url
    #
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
    
    1.Scrapy schedules the scrapy.Request obj returned by start_request method.
    2.Then after it recives a response, it instantiates response obj.
    3.Now it calls the callback method associated with request, passing the response obj as arg.       \
        
    so Request obj => Response obj => callback to associated method
    '''
    
    

    #3. Handling the urls:
    def parse(self, response):
        #This method will handle the response downloaded for each request made. Also finding new URLs to follow.
        #This is where we'll parse the scraped data the way we like.    
        page = response.url.split("/")[-2] # response.url : To get url of the response obj as string.
    
        #To extract page number which is the 
        #split the url with "/" as delim, which will split the url into a list , 
        #now take the second item from the end of the list, so we get the page number.
    
        #4. Extracting data:

        # To try out selectors using shell :
        # $ scrapy shell 'http://quotes.toscrape.com/page/1'
        # Selectors are patterns that match against elements in a tree.
        #view(response) : to find proper CSS selectors to use.

        #lets find author name and quote from quotestoscrape:
    
        #1 lets create array of all quotes:
        quotes = response.css('div.quote')
        # here we'll get selector list obj for all <div class="quote"> type tags.
        #which will contain all the tags matching the query .

        


        #now for each quotes let's dig deeper :

        # now each quotes element can be seen as like it is at the start of  <div class="quote">
        #so further (as per the layout of website) we can find the quote (<span class="text">) and the author (<span> <small class="author">)
        # so for each element of quote we'll do : 

        #list_of_quotes=[]
        #this list will contain dictionary with quote list and author pair.
                      
        #why is this now working ?
        #coz we ain't doing it the scarpy way...prob
        #so Scrapy uses yield keyword ..
        #scrapy generated many dictionaries

        '''for quote in quotes:
            dic_.clear()
            author = quote.css("span small.author::text").get()
            quote_ = quote.css('div.text::text').get() 
            dic_['quote'] = quote
            dic_['author'] = author
            list_of_quotes.append(dic_)
            #list_of_quotes.append(dict(zip(quote,author)))
        '''


        for quote in quotes:
            yield{
                'quote':quotes.css('span.text::text').get(),
                'author':quotes.css('span small.author::text').get()
            }   
        
'''   
-To run spider :
    $ scrapy crawl Spidy
    *From quotesScrape dir
-To store data :
    -use Feed exports:
    
    $ scrapy crawl Spidy -O fileName.json

    ** -O will overwrite any existing file
       -o will append new content to any existing file
'''


