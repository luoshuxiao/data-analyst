# -*- coding: utf-8 -*-
import pymysql


class AirplanePipeline(object):
    """构造一个mysql管道类"""
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = "insert into data (FlightNo,FlightCompany,FlightDeptimePlanDate,FlightArrtimePlanDate," \
              "CheckinTable,BaggageID,FlightDep,FlightArr,FlightDepAirport,FlightArrAirport,generic," \
              "DepWeather,ArrWeather,distance) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        self.cursor.execute(sql,
                            (item['FlightNo'], item['FlightCompany'], item['FlightDeptimePlanDate'],
                             item['FlightArrtimePlanDate'], item['CheckinTable'], item['BaggageID'],
                             item['FlightDep'], item['FlightArr'], item['FlightDepAirport'],
                             item['FlightArrAirport'], item['generic'], item['DepWeather'],
                             item['ArrWeather'], item['distance']))
        self.db.commit()
        return item
