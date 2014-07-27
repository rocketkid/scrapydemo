# This is an example of a Basic Spider

from scrapy.http.request import Request
from scrapy.spider import Spider
from scrapydemo.items import ExampleItem

class ExampleSpider(Spider):
	name = 'example'
	allowed_domains = ['example.com']
	start_urls = [
		'http://www.example.com/',
	]

	def parse(self, response):
		for h1 in response.xpath('//h1/text()').extract():
			yield ExampleItem(title = h1)

		for url in response.xpath('//a/@href').extract():
			yield Request(url, callback=self.parse)