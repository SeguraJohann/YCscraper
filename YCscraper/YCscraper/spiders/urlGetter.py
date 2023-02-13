import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options
import time


class MySpider(scrapy.Spider):
    name = 'urlGetter'
    start_urls = ['https://www.ycombinator.com/companies?isHiring=true&regions=Fully%20Remote']

    def __init__(self):
        options = Options() 
        options.headless = True
        options.page_load_strategy = 'eager'
        #options.add_argument("--headless=new") #to do: not sure if it's necessary, it works without it
        self.driver = webdriver.Chrome(options=options)
        
    def parse(self, response):
        
        self.driver.get(response.url)
        time.sleep(5) #to do: wait for the site to load, not sure if it is the most effective way, but as it is a small script I also don't think it worth the effor to figure it out 
        for i in range(15): #not sure how to make it scroll until there's no more, but as it is a small script I also don't think it worth the effor to figure it out
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sel = Selector(text=self.driver.page_source)
        links = sel.css('a.WxyYeI15LZ5U_DOM0z8F::attr(href)').getall() #css picker for companies urls 
        #print(links)
        with open('urls.txt', 'a') as f:
            for link in links:
                f.write("https://www.ycombinator.com" +link + '/jobs\n')

    def closed(self, reason):
        self.driver.quit()
            
