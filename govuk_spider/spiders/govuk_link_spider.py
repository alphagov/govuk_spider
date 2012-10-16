from urllib2 import urlopen
from xml.etree import ElementTree

from scrapy.contrib.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from govuk_spider.items import GovUKItem, SimpleLinkItem

def fetch_sitemap():
    url = "https://www.gov.uk/sitemap.xml"
    response = urlopen(url).read()
    root = ElementTree.fromstring(response)

    urls = ["https://www.gov.uk", "https://www.gov.uk/specialist"]
    for url in root:
        for loc in url:
            urls.append(loc.text)
        return urls

class GovUKLinkSpider(CrawlSpider):
    name = "gov.uk"
    start_urls = fetch_sitemap()
    rules = [
        Rule(SgmlLinkExtractor(allow=[r"businesslink\.gov\.uk/*"]),
             follow=False,
             callback="link_callback"),
        Rule(SgmlLinkExtractor(allow=[r"direct\.gov\.uk/*"]),
             follow=False,
             callback="link_callback"),
        Rule(SgmlLinkExtractor(allow=[r"www.gov.uk/*"],
                               deny=[r"www.gov.uk/business-finance-support-finder/*",
                                     r"www.gov.uk/licence-finder/*",
                                     r"www.gov.uk/trade-tariff/*"]),
             follow=True,
             callback="govuk_link_callback"),

        # Static links (CSS, JS).
        Rule(SgmlLinkExtractor(tags="link"),
             follow=True,
             callback="link_callback"),

        # All other generic links which don"t match those listed here.
        Rule(SgmlLinkExtractor(deny=[r"www.gov.uk/*",
                                     r"direct\.gov\.uk/*",
                                     r"businesslink\.gov\.uk/*"]),
             follow=False,
             callback="link_callback"),
        ]

    def link_callback(self, response):
        return SimpleLinkItem(url=response.url,
                              status=response.status,
                              referrer=response.request.headers.get("Referer"))

    def govuk_link_callback(self, response):
        """
        If the given page on www.gov.uk has a related links box, keep track
        of the count so that we know which pages have missing related links.
        """
        html = HtmlXPathSelector(response)
        related_links = html.select("//div[@class='related']/*/nav[@role='navigation']/ul/li").extract()
        if len(related_links) > 0:
            return GovUKItem(url=response.url,
                             status=response.status,
                             referrer=response.request.headers.get("Referer"),
                             related_link_count=len(related_links))
        else:
            return SimpleLinkItem(url=response.url,
                                  status=response.status,
                                  referrer=response.request.headers.get("Referer"))
