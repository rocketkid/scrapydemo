from scrapy.item import Item, Field

# Represent items scrapped from example.com
class ExampleItem(Item):
	title = Field()

# Represent items scrapped from dmoz.org
class DmozItem(Item):
	name = Field()
	url = Field()
	description = Field()


# Represent items scrappped from mininova.org
class TorrentItem(Item):
	url = Field()
	name = Field()
	description = Field()
	size = Field()

