import scrapy


class etfWatchSpider(scrapy.Spider):
    name = "etf-watch"

    def start_requests(self):
        urls = [
            'http://www.etfwatch.com.au/fundsearch/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        content = response.body
        file_name = 'output/etf-watch.html'
        self.save_html(file_name, content)

        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            ticker = row.xpath("./td[1]/a/text()").extract_first().strip()
            fund_name = row.xpath("./td[2]/a/text()").extract_first().strip()

            yield {
                "ticket": ticker,
                "fund_name": fund_name}

    def save_html(self, file_name, content):
        with open(file_name, 'wb') as f:
            f.write(content)
        self.log('Saved file %s' % file_name)
