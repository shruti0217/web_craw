# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class QuotescrapePipeline:
    #as item pass through pipline , search for initialization method.
    def __init__(self):
        self.connect_DB()
        self.create_TB()
    
    
    def connect_DB(self):
        connec = sqlite3.connect('Quotes.db')
        #self.connec = sqlite3.connect('Quotes.db')  #Throws error :/ why ?
        self.curr = connec.cursor()
    def create_TB(self):
        self.curr.execute('''DROP table if EXISTS Quotes_table''')
        self.curr.execute('''create table Quotes_table(author text, quote  text)''')
    def store_DB(self, item):
        self.curr.execute(''''insert into Quotes_table(?,?)''',(item['author'],item['quote']))

    
    def process_item(self, item, spider):
        #This method will be called automatically.    
        print('\n In the pipeline')
        self.store_DB(self,item)
        #return item
