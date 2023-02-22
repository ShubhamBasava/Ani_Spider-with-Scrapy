import scrapy

class AniSpider(scrapy.Spider):
    name = 'AniSpider'
    allowed_domains = ['myanimelist.net']
    start_urls = ['https://myanimelist.net/topanime.php']

    def parse(self, response):
        anime_links = response.css('.hoverinfo_trigger::attr(href)').extract()
        for link in anime_links:
            yield scrapy.Request(response.urljoin(link + '/reviews'), callback=self.parse_reviews)

    def parse_reviews(self, response):
        user_reviews = response.css('.borderDark').extract()
        for review in user_reviews:
            yield {'review': review}
