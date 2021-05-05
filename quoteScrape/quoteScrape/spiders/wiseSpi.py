import scrapy
from ..items import QuotescrapeItem
from scrapy.http import FormRequest

#importing the QuotescrapeItem from items.py so that we can pass 

#1 : Identifing target website:
#This spider will scrape quotes from : quotes.toscrape.com

class quotesSpi(scrapy.Spider):
    name = "Spidy"      #Identifies the spider

    #2 --------------: Collecting urls :------------
    #using start_request class attribute.
    #now this list will be used as default implementation of start_request().
    #To generate initial request.
    #Scrapy will call parse method for each urls.
    #coz parse is default callback method .
    
    start_urls = [
        "http://quotes.toscrape.com/login",
    

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
    3.Now it calls the callback method associated with request, passing the response obj as arg.       
        
    so Request obj => Response obj => callback to associated method
    
    **Basically response obj is nothing but the whole html of the site ...with some more methods added by scrapy.
    
    '''
    
    

    #--------------3.: Handling the urls:--------------
    #-----------------logging in--------------------
    def parse(self, response):
        #Usuallythis is where we'll parse the scraped data the way we like.
        #     
       
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'Someones@Email.com',
            'password':'somesName'
        },callback=self.scrape_begins)
        
    '''def yield_item(self,quote):
        #Yield items 
        item = QuotescrapeItem()
        item['author']=quote.css('span small.author::text').get()#Just this damn lil error 
        #USE '=' and NOT ':'
        item['quote']=quote.css('span.text::text').get()
        item['tags']=quote.css('.tag::text').get()
        
        yield item'''
        # Now this item will be sent to items.py then to pipelines.py 
        #Coz we enabled piplines 
             
        


    def scrape_begins(self,response):
        #This method will handle the response downloaded for each request made. Also finding new URLs to follow.
        
        #---------------4. Extracting data:-----------

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
        
        
        #here we'll use the passed author to crape the data:
        #author = getattr(self, author,None)
        author_ = self.author
        author_=author_.lower().split(',')
        author_list = [a.strip() for a in author_]
        print(author_)
        
        item = QuotescrapeItem()    #instance of QuotescrapeItem 

        
        for quote in quotes :
            if 'all' in author_list:
                item['author']=quote.css('span small.author::text').get()#Just this damn lil error 
                #USE '=' and NOT ':'
                item['quote']=quote.css('span.text::text').get()
                item['tags']=quote.css('.tag::text').get()
                yield item
                #yield_item(quote)                     
            elif quote.css('span small.author::text').get().lower() in author_list :
                item['author']=quote.css('span small.author::text').get()#Just this damn lil error 
                item['quote']=quote.css('span.text::text').get()
                item['tags']=quote.css('.tag::text').get()
                yield item
                
                
                
        #5.Following links:
        # 
        #let's first scrape the links from the web page:
        
        next_page = response.css('li a::attr(href)').get()
        
        # Now if we did get link fom the given page then we have to generate a request obj then instantiate the response object and then callback parse as we did before !
        #if next_page is not None:
            #next_page = response.urljoin(next_page) # what does this do ? 
            #       we join the the url we had in response obj with the next_page and now we got a full link to the next page
            #       urljoin() coz links can be relative.
            #yield scrapy.Request(next_page,callback= self.parse) # Request the page and call parse with respond obj
            #       and now our spidy follows links 

        '''
            Scrapy shedule the request to be sent and registers a callback method to be executed.
            
            
        '''
            #------:Short cut for creating requests :
        if next_page is not None:
            yield response.follow(next_page,callback = self.scrape_begins)
            #Unlike scrapy.request response.follow supports relative links so no need to perform urljoin.
            '''****it returns a Request instance.'''
            # *** for <a> it automatically use it's href attribute !
            # so we can do :
            # for a in reponse.css('ul.pager a'):
            #   yield response.follow(a,callback=self.parse)
            
        #reponse.follow_all(a,callback = self.parse): alternative to follow request from iterable .
        #a = response.css('ul.pager a')
        #yield from response.follow_all(a, callback= self.parse)
        #
        #yield from response.follow_all(css='ul.pager a',callback = self.parse)
    '''

    '''
'''         
-To run spider :
    $ scrapy crawl Spidy
    *From quotesScrape dir
-To store data :
    -use Feed exports:
    
    $ scrapy crawl Spidy -O fileName.json -a author='Author1 Name,Author2 Name'

    ->author = 'all' : to scrape all authors
    

    ** -O will overwrite any existing file
       -o will append new content to any existing file
'''


