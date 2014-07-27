# Pipelines

import MySQLdb

class DmozItemStorePipeline(object):
	ADD_ITEM_QUERY = ("INSERT INTO DMOZ_ITEMS "
			"(name, url, description) "
			"VALUES (%s, %s, %s)"
			)

	def __init__(self):
		db_host = settings['MYSQL_HOST']
		db_name = settings['MYSQL_DBNAME']
		db_user = settings['MYSQL_USER']
		db_password = settings['MYSQL_PASSWD']
        
        self.db = MySQLdb.connect( db_host, db_user, db_password, db_name)
        self.dbc = self.db.cursor() 

    def process_item(self, item, spider):
    	add_item_data = (item['name'], item['url'], item['description'])
    	self.dbc.execute(ADD_ITEM_QUERY, add_item_data)
    	return item


