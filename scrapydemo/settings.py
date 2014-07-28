BOT_NAME = 'scrapydemo'

SPIDER_MODULES = ['scrapydemo.spiders']
NEWSPIDER_MODULE = 'scrapydemo.spiders'

#ITEM_PIPELINES = ['scrapydemo.pipelines.DmozItemStorePipeline']
ITEM_PIPELINES = {
    'scrapydemo.pipelines.DmozItemStorePipeline': 1   
}

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapydemo'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''


