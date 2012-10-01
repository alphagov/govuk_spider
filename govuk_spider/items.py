from scrapy.item import Item, Field

class SimpleLinkItem(Item):
    url = Field()
    status = Field()
    referrer = Field()

class GovUKItem(SimpleLinkItem):
    related_link_count = Field()
