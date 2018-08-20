import scrapy
from metacritic.items import MetacriticItem

class metacritic(scrapy.Spider):
    name = "my_scraper"
    start_urls = ["http://www.metacritic.com/browse/albums/score/metascore/all/filtered"]
    npages = 3
    # This mimics getting the pages using the next button
    for i in range(1, npages + 1):
        start_urls.append("http://www.metacritic.com/browse/albums/score/metascore/all/filtered?page="+str(i)+"")    
    def parse(self, response):
        for href in response.xpath("//div[contains(@class, 'product_title')]/a//@href"):
            # add the scheme, eg http://
            url  = "http://www.metacritic.com/" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)
    
    def parse_dir_contents(self, response):
        item = MetacriticItem()
        # Getting album
        item['album'] = response.xpath("//span[contains(@itemprop,'name')]/h1/text()").extract_first()
        # Getting artist
        item['artist']= response.xpath("//span[contains(@class,'band_name')]/text()").extract_first()
        # User score
        item['userscore'] = response.xpath("//div[contains(@class,'metascore_w user large')]/text()").extract_first()
        # meta Score
        item['metascore'] = response.xpath("//span[contains(@itemprop,'ratingValue')]/text()").extract_first()
        # Release Date
        item['releasedate'] = response.xpath("//span[contains(@itemprop,'datePublished')]/text()").extract()
        #genre
        item['genre'] = response.xpath("//span[contains(@itemprop,'genre')]/text()").extract()
        
        yield item