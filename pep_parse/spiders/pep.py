import scrapy
from .items import PepParsingItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        rows = response.css('tr')
        for row in rows:
            if (row.css('abbr::text').get() and row.css('a::text').getall()):

                data = {
                    'status': row.css('abbr::text').get(),
                    'number': row.css('a::text').getall()[0],
                    'pep': row.css('a::text').getall()[1]
                }
                yield PepParsingItem(data)

            url_pep = row.css('a').attrib['href']
