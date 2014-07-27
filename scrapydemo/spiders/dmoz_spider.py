from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapydemo.items import DmozItem


class DmozSpider(Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		selector = Selector(response)
		sites = selector.xpath('//ul[@class="directory-url"]/li')
		items = []

		for site in sites:
			item = DmozItem()
			item['name'] = site.xpath('a/text()').extract()
			item['url'] = site.xpath('a/@href').extract()
			item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
			items.append(item)
		return items
