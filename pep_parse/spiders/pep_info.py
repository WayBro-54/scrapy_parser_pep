import scrapy


class PepInfoSpider(scrapy.Spider):
    name = 'pep_info'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        rows = response.css('tr')
        for row in rows:
            if (row.css('abbr::text').get() and row.css('a::text').getall()):
                pep_url = row.css('a').attrib['href']
                yield response.follow(url=pep_url, callback=self.parse_info)

    def parse_info(self, response):
        status_info = response.xpath(
            "//dl[@class='rfc2822 field-list simple']/dd[@class='field-odd']/abbr/text()")
