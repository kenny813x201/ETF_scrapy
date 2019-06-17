import scrapy


class xratesSpider(scrapy.Spider):
    name = "x-rates"

    def start_requests(self):
        url = "https://www.x-rates.com/table"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.css("table.ratesTable tbody tr"):
            yield {
                "currency": row.xpath("./td[1]/text()").extract(),
                "oneUSD": row.xpath("./td[2]/a/text()").extract(),
                "inverseOneUSD": row.xpath("./td[3]/a/text()").extract(),
            }
