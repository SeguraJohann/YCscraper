import scrapy

class JobSpider(scrapy.Spider):
    name = "newGrads"

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
            if "Any (new grads ok)" in jobElements.extract():
                jobUrl = jobElements.xpath('.//a/@href').get()
                with open('new_grad_jobs.txt', 'a') as f:
                    print("https://www.ycombinator.com" + jobUrl + '\n')
                    f.write("https://www.ycombinator.com" + jobUrl + '\n')
            
