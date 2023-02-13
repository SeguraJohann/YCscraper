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
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        
    def parse(self, response):
        
        self.driver.get(response.url)
        time.sleep(5)
        for i in range(15):
            print(i)
            
