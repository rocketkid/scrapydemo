# This is an example of an XMLFeed Spider

from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider
from scrapydemo.items import BreakfastItem

class W3SchoolSpider(XMLFeedSpider):
	name = "w3schools"
	allowed_domains = ['w3schools.com']
	start_urls = ['http://www.w3schools.com/xml/simple.xml']

	iterator = 'iternodes'
	itertag = 'food'

	def parse_node(self, response, node):
		item = BreakfastItem()
		item['name'] = node.xpath('name/text()').extract()
		item['description'] = node.xpath('description/text()').extract()
		item['price'] = node.xpath('price/text()').extract()
		item['calories'] = node.xpath('calories/text()').extract()
		return item

