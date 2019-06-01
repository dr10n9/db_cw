import scrapy
import pymongo
from pymongo import ReadPreference

# connection = pymongo.MongoClient([
#     'localhost:27017',
#     'localhost:27018',
#     'localhost:27019'
# ],replicaset='replica1')
connection = pymongo.MongoClient("localhost:27010")

db = connection.get_database('cw', read_preference=ReadPreference.SECONDARY)

USD = 26.34
EUR = 29.512

class MuztorgScrapy(scrapy.Spider):
    i = 0   

    name = 'muztorg'

    def start_requests(self):
        guitars = [
            'https://muztorg.ua/gitari/jelektrogitara?limit=100&mfp=112-[%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%B3%D0%B8%D1%82%D0%B0%D1%80%D1%8B]',
            'https://muztorg.ua/gitari/jelektrogitara?limit=100&mfp=112-[%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%B3%D0%B8%D1%82%D0%B0%D1%80%D1%8B]&page=2',
            'https://muztorg.ua/gitari/jelektrogitara?limit=100&mfp=112-[%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%B3%D0%B8%D1%82%D0%B0%D1%80%D1%8B]&page=3'
        ]
        for url in guitars:
            yield scrapy.Request(url=url, callback=self.parse_guitars)

    def parse_guitars(self, response):
        print(f'COUNTER {self.i}')
        self.i+=1
        page = response.url.split("/")[-2]
        product_blocks = response.css('div.product-layoutcat')
        
        for block in product_blocks:
            price = block.xpath('.//p[@class="price"]/text()').extract()[0].strip()
            if len(price) == 0:
                price = block.xpath('.//p[@class="price"]/span[@class="price-old"]/text()').extract()[0].strip()
            
            price = str(price).split(' ')[0]
            price = round(float(price)/EUR, 2)

            name = block.xpath('.//img[@class="img-responsive center-add_img"]/@title').extract()[0].strip()
            name_arr = str(name).split('by')

            manufacturer = None
            model = None

            if len(name_arr) == 2:
                manufacturer = name_arr[1].strip().split(' ')[0].capitalize()
                print(manufacturer)
                model = name_arr[0] + ' '.join(name_arr[1].strip().split(' ')[1:-1])
            else:
                name = str(name).split(' ')
                manufacturer = name[0]
                model = ' '.join(name[1:-1])

            data = {
                'manufacturer': manufacturer,
                'model': model,
                'price': price,
                'source': self.name
            }
            print(data)
            db.guitars.insert_one(data)
    
    def parse_drums(self, response):
        """"""