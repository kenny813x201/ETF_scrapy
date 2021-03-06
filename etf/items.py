# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EtfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ticker = scrapy.Field()
    url = scrapy.Field()
    fund_name = scrapy.Field()
    fund_type = scrapy.Field()
    mgmt_type = scrapy.Field()
    fund_manager = scrapy.Field()
    market_cap = scrapy.Field()
    mgmt_cost = scrapy.Field()
    performance_fees = scrapy.Field()
    inception_date = scrapy.Field()
    price = scrapy.Field()
    one_month = scrapy.Field()
    three_month = scrapy.Field()
    year_to_date = scrapy.Field()
    one_year = scrapy.Field()
    three_year_pa = scrapy.Field()
    five_year_pa = scrapy.Field()
    ten_year_pa = scrapy.Field()
    annual_yield = scrapy.Field()
    franking = scrapy.Field()
    last_dividend_ex_date = scrapy.Field()
    last_dividend_paid_date = scrapy.Field()
    last_dividend_amount = scrapy.Field()
    dividend_frequency = scrapy.Field()
    region = scrapy.Field()
    industry = scrapy.Field()
    focus = scrapy.Field()
    currency_hedge = scrapy.Field()
    benchmark = scrapy.Field()
    investment_style = scrapy.Field()
    nav_pre_tax = scrapy.Field()
    nav_post_tax = scrapy.Field()
    nav_premium_pre_tax = scrapy.Field()
    nav_premium_post_tax = scrapy.Field()
    nav_date = scrapy.Field()

    pass
