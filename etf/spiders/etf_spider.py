import scrapy


class QuotesSpider(scrapy.Spider):
    name = "etf"

    def start_requests(self):
        urls = [
            'https://etfdb.com/screener/#page=2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text = response.body.decode().replace(
            "<!--[if lte IE 9]>", "").replace("<!--<![endif]--><!-->", "")
        response = scrapy.Selector(text=text)
        file_name = 'output/etf.html'
        self.save_html(file_name, text)

        def remove_newline(text):
            return text.replace("\n", "")

        rows = response.xpath("//div/table//tbody/tr")
        for row in rows:
            symbol = row.xpath(
                "./td[@data-th='Symbol']/a/text()").extract_first()
            etf_name = row.xpath(
                "./td[@data-th='Name']/a/text()").extract_first()
            price = row.xpath("./td[@data-th='Price']/text()").extract_first()
            assets = row.xpath(
                "./td[@data-th='Assets']/text()").extract_first()
            average_volume = row.xpath(
                "./td[@data-th='Average volume']/text()").extract_first()
            ytd = row.xpath("./td[@data-th='Ytd']/text()").extract_first()
            asset_class = row.xpath(
                "./td[@data-th='Asset class']/text()").extract_first()

            yield {
                # "row": row.extract(),
                "symbol": remove_newline(symbol),
                "etf_name": remove_newline(etf_name),
                "price": remove_newline(price),
                "assets": remove_newline(assets),
                "average_volume": remove_newline(average_volume),
                "ytd": remove_newline(ytd),
                "asset_class": remove_newline(asset_class),
            }

    def save_html(self, file_name, content):
        with open(file_name, 'wb') as f:
            f.write(content.encode())
        self.log('Saved file %s' % file_name)
