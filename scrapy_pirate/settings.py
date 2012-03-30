# Scrapy settings for scrapy_pirate project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapy_pirate'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrapy_pirate.spiders']
NEWSPIDER_MODULE = 'scrapy_pirate.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

