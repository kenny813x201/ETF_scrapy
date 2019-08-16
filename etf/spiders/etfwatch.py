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
            fund_type = row.xpath(
                "./td[3]/span/text()").extract_first().strip()
            mgmt_type = row.xpath(
                "./td[4]/span/text()").extract_first().strip()
            fund_manager = row.xpath(
                "./td[5]/span/text()").extract_first().strip()
            market_cap = row.xpath(
                "./td[6]/span/text()").extract_first().strip()
            mgmt_cost = row.xpath(
                "./td[7]/span/text()").extract_first().strip()
            performance_fees = row.xpath(
                "./td[8]/span/text()").extract_first().strip()
            inception_date = row.xpath(
                "./td[9]/span/text()").extract_first().strip()
            price = row.xpath(
                "./td[@class='performance'][2]/span/text()").extract_first().strip()
            one_month = row.xpath(
                "./td[@class='performance'][3]/span/text()").extract_first().strip()
            three_month = row.xpath(
                "./td[@class='performance'][4]/span/text()").extract_first().strip()
            year_to_date = row.xpath(
                "./td[@class='performance'][5]/span/text()").extract_first().strip()
            one_year = row.xpath(
                "./td[@class='performance'][6]/span/text()").extract_first().strip()
            three_year_pa = row.xpath(
                "./td[@class='performance'][7]/span/text()").extract_first().strip()
            five_year_pa = row.xpath(
                "./td[@class='performance'][8]/span/text()").extract_first().strip()
            ten_year_pa = row.xpath(
                "./td[@class='performance'][9]/span/text()").extract_first().strip()
            annual_yield = row.xpath(
                "./td[@class='dividends'][1]/span/text()").extract_first().strip()
            franking = row.xpath(
                "./td[@class='dividends'][2]/span/text()").extract_first().strip()
            last_dividend_ex_date = row.xpath(
                "./td[@class='dividends'][3]/span/text()").extract_first().strip()
            last_dividend_paid_date = row.xpath(
                "./td[@class='dividends'][4]/span/text()").extract_first().strip()
            last_dividend_amount = row.xpath(
                "./td[@class='dividends'][5]/span/text()").extract_first().strip()
            dividend_frequency = row.xpath(
                "./td[@class='dividends'][6]/span/text()").extract_first().strip()
            region = row.xpath(
                "./td[@class='classification'][1]/span/text()").extract_first().strip()
            industry = row.xpath(
                "./td[@class='classification'][2]/span/text()").extract_first().strip()
            focus = row.xpath(
                "./td[@class='classification'][3]/span/text()").extract_first().strip()
            currency_hedge = row.xpath(
                "./td[@class='classification'][4]/span/text()").extract_first().strip()
            benchmark = row.xpath(
                "./td[@class='classification'][5]/span/text()").extract_first().strip()
            investment_style = row.xpath(
                "./td[@class='classification'][6]/span/text()").extract_first().strip()
            nav_pre_tax = row.xpath(
                "./td[@class='net-asset-value'][1]/span/text()").extract_first().strip()
            nav_post_tax = row.xpath(
                "./td[@class='net-asset-value'][2]/span/text()").extract_first().strip()
            nav_premium_pre_tax = row.xpath(
                "./td[@class='net-asset-value'][3]/span/text()").extract_first().strip()
            nav_premium_post_tax = row.xpath(
                "./td[@class='net-asset-value'][4]/span/text()").extract_first().strip()
            nav_date = row.xpath(
                "./td[@class='net-asset-value'][5]/span/text()").extract_first().strip()


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
            items['price'] = price
            items['one_month'] = one_month
            items['three_month'] = three_month
            items['year_to_date'] = year_to_date
            items['one_year'] = one_year
            items['three_year_pa'] = three_year_pa
            items['five_year_pa'] = five_year_pa
            items['ten_year_pa'] = ten_year_pa
            items['annual_yield'] = annual_yield
            items['franking'] = franking
            items['last_dividend_ex_date'] = last_dividend_ex_date
            items['last_dividend_paid_date'] = last_dividend_paid_date
            items['last_dividend_amount'] = last_dividend_amount
            items['dividend_frequency'] = dividend_frequency
            items['region'] = region
            items['industry'] = industry
            items['focus'] = focus
            items['currency_hedge'] = currency_hedge
            items['benchmark'] = benchmark
            items['investment_style'] = investment_style
            items['nav_pre_tax'] = nav_pre_tax
            items['nav_post_tax'] = nav_post_tax
            items['nav_premium_pre_tax'] = nav_premium_pre_tax
            items['nav_premium_post_tax'] = nav_premium_post_tax
            items['nav_date'] = nav_date

            yield items

    def save_html(self, file_name, content):
        with open(file_name, 'wb') as f:
            f.write(content)
        self.log('Saved file %s' % file_name)
