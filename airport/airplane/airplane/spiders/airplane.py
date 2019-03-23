# -*- coding: utf-8 -*-
import json
import time

import scrapy

from airplane.items import AirplaneItem


class AirplaneSpider(scrapy.Spider):
    name = 'airplane'
    allowed_domains = ['www.variflight.com']
    start_urls = ['http://webapp.veryzhun.com/h5/flightsearch?arr=PVG&dep=CTU&date=2019-03-14&token=74e5d4cac3179fc076af4f401fd4ebe3&limityzm=uc2147']

    def start_requests(self):
        time_today = time.time() - 24 * 60 * 60
        time.strftime('%Y-%m-%d', time.localtime(time.time()))
        start_t = '2016-01-01 00:00:00'
        start_t_t = time.mktime(time.strptime(start_t,'%Y-%m-%d %H:%M:%S'))
        url = ''
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        results_json = response.text
        results_list = json.loads(results_json)
        print(results_list)
        for item in results_list:
            air = AirplaneItem()
            air['FlightNo'] = item['FlightNo']
            air['FlightCompany'] = item['FlightCompany']
            air['FlightDeptimePlanDate'] = item['FlightDeptimePlanDate']
            air['FlightArrtimePlanDate'] = item['FlightArrtimePlanDate']
            air['CheckinTable'] = item['CheckinTable']
            air['BaggageID'] = item['BaggageID']
            air['FlightDep'] = item['FlightDep']
            air['FlightArr'] = item['FlightArr']
            air['FlightDepAirport'] = item['FlightDepAirport']
            air['FlightArrAirport'] = item['FlightArrAirport']
            air['generic'] = item['generic']
            air['DepWeather'] = item['DepWeather']
            air['ArrWeather'] = item['ArrWeather']
            air['distance'] = item['distance']
            yield air
