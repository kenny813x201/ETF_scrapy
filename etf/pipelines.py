# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import pymongo
from cloud.firebase import Firebase_connection
from cloud.dynamodb import DynamoDB_connection


class SqlitePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("output/etf.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS etf_db""")
        self.curr.execute("""CREATE TABLE etf_db(
                        ticker text,
                        url text,
                        fund_name text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO etf_db VALUES (?,?,?)""", (
            item['ticker'],
            item['url'],
            item['fund_name']
        ))
        self.conn.commit()


class MongoPipeline(object):
    collection_name = 'etf_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'ETF')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        if self.collection_name in self.db.list_collection_names():
            self.db.drop_collection(self.collection_name)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


class FirebasePipeline(object):

    firebase_client = Firebase_connection()

    def process_item(self, item, spider):

        exists = self.firebase_client.check_doc_exist(item)
        if exists:
            self.firebase_client.update_doc(item)
        else:
            self.firebase_client.add_doc(item)

        return item


class DynamoDBPipeline(object):

    dynamodb_client = DynamoDB_connection()

    def process_item(self, item, spider):
        self.dynamodb_client.add_doc(item)

        return item
