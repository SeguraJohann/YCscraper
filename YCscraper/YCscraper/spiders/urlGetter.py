import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options

class MySpider(scrapy.Spider):
    name = 'urlGetter'
    start_urls = ['https://www.ycombinator.com/companies?isHiring=true&regions=Fully%20Remote']

    def __init__(self):
