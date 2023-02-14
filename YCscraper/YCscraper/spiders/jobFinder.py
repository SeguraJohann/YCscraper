import scrapy

class JobSpider(scrapy.Spider):
    name = "jobFinder"

    def start_requests(self):
        urls = []
        with open('urls.txt', 'r') as f:
            for line in f:
                urls.append(line.strip())
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        print(urls)

    def parse(self, response):
        jobElements = response.xpath('//div[@class="flex w-full flex-row justify-between py-4"]')
        for job in jobElements:
            print (job)
