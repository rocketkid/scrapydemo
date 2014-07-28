# Pipelines

import MySQLdb
from scrapy.exceptions import DropItem

class DmozItemStorePipeline(object):

    def __init__(self, db_conn):
    	self.db_conn = db_conn
    	self.db_cursor = db_conn.cursor()

    @classmethod
    def from_settings(cls, settings):
    	db_host = settings['MYSQL_HOST']
    	db_name = settings['MYSQL_DBNAME']
    	db_user = settings['MYSQL_USER']
    	db_passwd = settings['MYSQL_PASSWD']

        db_conn = MySQLdb.connect(db_host, db_user, db_passwd, db_name)
        return cls(db_conn)

    def process_item(self, item, spider):
        name = ''.join(item['name'])
        url = ''.join(item['url'])
        description = ''.join(item['description'])

    	try:
            self.db_cursor.execute('''INSERT INTO DMOZ_ITEMS (name, url, description) VALUES (%s, %s, %s)''', (name, url, description))
            self.db_conn.commit()
            return item
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            self.db_conn.rollback()
            raise DropItem("Unable to insert item: %s" % item)

       
