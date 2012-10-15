# Scrapy settings for govuk_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'govuk_spider'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['govuk_spider.spiders']
NEWSPIDER_MODULE = 'govuk_spider.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'govuk_spider.pipelines.DuplicatesPipeline',
]

DOWNLOAD_DELAY = 1.0 # 1000ms delay
CONCURRENT_REQUESTS_PER_DOMAIN = 4
