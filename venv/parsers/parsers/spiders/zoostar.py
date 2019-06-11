import scrapy
 
class zoostar(scrapy.Spider):
    name = 'zoostar'
    pet = ''
    def start_requests(self):
 
        cat_goods = [
            'https://zoostar.ua/catalog/dry-feed-for-cats',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=2',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=3',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=4',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=5'
        ]
 
        dog_goods = [
            'https://zoostar.ua/catalog/dry-feed-for-dogs',
            'https://zoostar.ua/catalog/dry-feed-for-dogs?page=2',
            'https://zoostar.ua/catalog/dry-feed-for-dogs?page=3',
            'https://zoostar.ua/catalog/dry-feed-for-dogs?page=4',
            'https://zoostar.ua/catalog/dry-feed-for-dogs?page=5'
        ]
 
        self.type_goods = 'dry food'
        for url in dog_goods:
            self.pet = 'dog'
            yield scrapy.Request(url=url, callback=self.parse)
 
        self.pet = 'cat'
        for url in cat_goods:
            yield scrapy.Request(url=url, callback=self.parse)
 
 
 
    def parse(self, response):
        page = response.url.split("/")[-2]
        product_blocks = response.css('div.product-thumb')
        print(len(product_blocks))
        for block in product_blocks:
            name = block.xpath('.//div[@class="top"]/p[@class="prod_name"]/a/span/@title').extract()[0]
            manufacturer  = block.xpath('.//div[@class="top"]/a/span/text()').extract()[0]
            price = block.xpath('.//div[@class="price"]/span[@class="the_good_price"]/text()').extract()
            price = price[0].split(',')
            price = ''.join(price)
            price = price.split(' ')
            tmp = price
            for p in tmp:
                p = p.split('\xa0')
                for temp_p in p:                
                    try:
                        price = float(temp_p)
                    except Exception as e:
                        """"""
                    # print(e)
            data = {
                'pet': self.pet,
                'type goods': self.type_goods,
                'manufacturer': manufacturer,
                'name': name,
                'price': price
            }
            print(data)