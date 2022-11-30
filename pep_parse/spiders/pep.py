import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        rows = response.css('tr')
        urls = rows.css('a::attr(href)').getall()
        for url in urls:
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'status': response.xpath("//dd[@class='field-odd']/abbr/text()").get(),
            'number': response.xpath("//h1[@class='page-title']/text()").get().split()[1],
            'name': response.xpath("//h1[@class='page-title']/text()").get()
        }
        yield PepParseItem(data)
