import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        countries = response.xpath('//tbody//a/text()').getall()
        poblacion = response.xpath('//tbody/tr/td[3]/text()').getall()


        for pais, num in zip(countries, poblacion):
            info = {
                'Pais' : pais,
                'Poblacion' : num
            }

            yield info
        
        
       
