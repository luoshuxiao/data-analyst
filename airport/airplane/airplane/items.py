
import scrapy


class AirplaneItem(scrapy.Item):

    FlightNo = scrapy.Field()
    FlightCompany = scrapy.Field()
    FlightDeptimePlanDate = scrapy.Field()
    FlightArrtimePlanDate = scrapy.Field()
    CheckinTable = scrapy.Field()
    BaggageID = scrapy.Field()
    FlightDep = scrapy.Field()
    FlightArr = scrapy.Field()
    FlightDepAirport = scrapy.Field()
    FlightArrAirport = scrapy.Field()
    generic = scrapy.Field()
    DepWeather = scrapy.Field()
    ArrWeather = scrapy.Field()
    distance = scrapy.Field()

