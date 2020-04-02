import scrapy
import sys
from scrapy.spiders import CrawlSpider
from scrapy import Selector

sys.path.append("/Users/bradadams/Desktop/GoodReadsScraper/")

from GoodReadsScraper.items import GoodreadsscraperItem, ReviewLoader


class GoodReadsScraper(scrapy.Spider):
	name = "single_book_scraper"
	allowed_domains = ["https://www.goodreads.com"]
	start_urls = ["https://www.goodreads.com/book/show/51569514-ask-a-footballer"]

	def parse(self,response):
		l = ReviewLoader(item=GoodreadsscraperItem(), response = response)

		l.add_css('review','span[style*="display:none"]')

		return l.load_item()



#class GoodReadsScraper(scrapy.Spider):
#	name = "single_book_scraper"
#	allowed_domains = ["https://www.goodreads.com"]
#	start_urls = ["https://www.goodreads.com/book/show/51569514-ask-a-footballer"]
#	def parse(self,response):
#		for i in response.css('span[style*="display:none"]'):
#			yield {'review' : i.getall()}




#code to run: 
#cd ~/Desktop/GoodReadsScraper
#scrapy crawl single_book_scraper -o data.csv





