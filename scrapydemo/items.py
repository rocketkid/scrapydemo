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

# Represent item scapped from http://www.w3schools.com/xml/simple.xml
class BreakfastItem(Item):
	name = Field()
	price = Field()
	description = Field()
	calories = Field()
	
