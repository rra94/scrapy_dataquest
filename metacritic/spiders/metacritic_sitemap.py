from scrapy.spiders import SitemapSpider
from metacritic.items import MetacriticItem

class MySpider(SitemapSpider):
    name="sitemap_mc"
    sitemap_urls = ['http://www.metacritic.com/siteindex.xml']
    #sitemap_rules = [('/Album-music/', 'parse_category')]
    sitemap_follow = ['/Album-music']
    def parse(self, response):
        item = MetacriticItem()
        item['album'] = response.xpath("//span[contains(@itemprop,'name')]/h1/text()").extract_first()
        item['artist']= response.xpath("//span[contains(@class,'band_name')]/text()").extract_first()
        item['userscore'] = response.xpath("//div[contains(@class,'metascore_w user large')]/text()").extract_first()
        item['metascore'] = response.xpath("//span[contains(@itemprop,'ratingValue')]/text()").extract_first()
        item['releasedate'] = response.xpath("//span[contains(@itemprop,'datePublished')]/text()").extract()
        item['genre'] = response.xpath("//span[contains(@itemprop,'genre')]/text()").extract()
        yield item
