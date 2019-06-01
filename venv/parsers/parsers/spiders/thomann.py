import scrapy
# from src.entities.guitar import GuitarController
import pymongo
from pymongo import ReadPreference

connection = pymongo.MongoClient("localhost:27010")

db = connection.get_database('cw', read_preference=ReadPreference.SECONDARY)

class MuztorgScrapy(scrapy.Spider):
    name = 'thomann'

    def start_requests(self):
        guitars = [
            'https://www.thomann.de/intl/ua/st_models.html?ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=2&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=3&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=4&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=5&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=6&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=7&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=8&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=9&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=10&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=11&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=12&ls=100',
            'https://www.thomann.de/intl/ua/st_models.html?pg=13&ls=100',
            'https://www.thomann.de/intl/ua/t_models.html?ls=100',
            'https://www.thomann.de/intl/ua/t_models.html?pg=2&ls=100',
            'https://www.thomann.de/intl/ua/t_models.html?pg=3&ls=100',
            'https://www.thomann.de/intl/ua/t_models.html?pg=4&ls=100',
            'https://www.thomann.de/intl/ua/lp_models.html?ls=100',
            'https://www.thomann.de/intl/ua/lp_models.html?pg=2&ls=100',
            'https://www.thomann.de/intl/ua/lp_models.html?pg=3&ls=100',
            'https://www.thomann.de/intl/ua/lp_models.html?pg=4&ls=100',
            'https://www.thomann.de/intl/ua/lp_models.html?pg=5&ls=100',
            'https://www.thomann.de/intl/ua/lp_models.html?pg=6&ls=100',
            'https://www.thomann.de/intl/ua/sg_models.html?ls=100',
            'https://www.thomann.de/intl/ua/sg_models.html?pg=2ls=100',
            'https://www.thomann.de/intl/ua/sg_models.html?pg=3ls=100'
        ]
        for url in guitars:
            yield scrapy.Request(url=url, callback=self.parse_guitars)

    def parse_guitars(self, response):
        # print(response)
        blocks = response.css('div.extensible-article')
        for block in blocks:
            manufacturer = str(block.css('span.manufacturer').xpath('./text()').extract()[0].strip())
            model = (block.css('span.model').xpath('./text()').extract()[0].strip())
            price = str(block.css('span.article-basketlink').xpath('./text()').extract()[0].strip())[1:]
            price = price.split(',')
            price = float(''.join(price))
            data = {
                'manufacturer': manufacturer,
                'model': model,
                'price': price,
                'source': self.name
            }
            db.guitars.insert_one(data)
            # print(data)
        
        def parse_drums(self, response):
            """"""

        def parse_guitars(self, response):
            """"""