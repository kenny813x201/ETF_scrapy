import scrapy
from ..items import EtfItem


class etfWatchSpider(scrapy.Spider):
    name = "etf-watch"
    

    def start_requests(self):
        urls = [
            'http://www.etfwatch.com.au/fundsearch/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = EtfItem()

        content = response.body
        file_name = 'output/etf-watch.html'
        self.save_html(file_name, content)

        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            ticker = row.xpath("./td[1]/a/text()").extract_first().strip()
            url = row.xpath("./td[1]/a/@href").extract_first().strip()
            fund_name = row.xpath("./td[2]/a/text()").extract_first().strip()
            fund_type = row.xpath("./td[3]/span/text()").extract_first().strip()
            mgmt_type = row.xpath("./td[4]/span/text()").extract_first().strip()
            fund_manager = row.xpath("./td[5]/span/text()").extract_first().strip()
            market_cap = row.xpath("./td[6]/span/text()").extract_first().strip()
            mgmt_cost = row.xpath("./td[7]/span/text()").extract_first().strip()
            performance_fees = row.xpath("./td[8]/span/text()").extract_first().strip()
            inception_date = row.xpath("./td[9]/span/text()").extract_first().strip()

            items['ticker'] = ticker
            items['url'] = url
            items['fund_name'] = fund_name
            items['fund_type'] = fund_type
            items['mgmt_type'] = mgmt_type
            items['fund_manager'] = fund_manager
            items['market_cap'] = market_cap
            items['mgmt_cost'] = mgmt_cost
            items['performance_fees'] = performance_fees
            items['inception_date'] = inception_date
            
            yield items

    def save_html(self, file_name, content):
        with open(file_name, 'wb') as f:
            f.write(content)
        self.log('Saved file %s' % file_name)
