from scrapy.spider import Spider
from scrapydemo.items import ExampleItem

class ExampleSpider(Spider):
	name = 'example'
	allowed_domains = ['example.com']
	start_urls = [
		'http://www.example.com/',
	]

	def parse(self, response):
		self.log('A response from %s just arrived!' % response.url)
		item = ExampleItem()
		item['title'] = response.xpath('//h1/text()').extract()
		return item
