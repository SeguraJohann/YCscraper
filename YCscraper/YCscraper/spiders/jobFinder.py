import scrapy

class JobSpider(scrapy.Spider):
    name = "job_spider"

    def start_requests(self):
        urls = []

    def parse(self, response):
