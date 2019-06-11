import scrapy
 
class petco(scrapy.Spider):
    name = 'petco'
    def start_requests(self):
 
        cat_goods = [
            'https://zoostar.ua/catalog/dry-feed-for-cats',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=2',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=3',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=4',
            'https://zoostar.ua/catalog/dry-feed-for-cats?page=5'
        ]
 
        dog_goods = [
            'https://www.petco.com/shop/en/petcostore/category/dog/dog-food/dry-dog-food#facet:&productBeginIndex:0&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:24&',
            'https://www.petco.com/shop/en/petcostore/category/dog/dog-food/dry-dog-food#facet:&productBeginIndex:24&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:24&',
            'https://www.petco.com/shop/en/petcostore/category/dog/dog-food/dry-dog-food#facet:&productBeginIndex:48&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:24&',
            'https://www.petco.com/shop/en/petcostore/category/dog/dog-food/dry-dog-food#facet:&productBeginIndex:72&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:24&',
            'https://www.petco.com/shop/en/petcostore/category/dog/dog-food/dry-dog-food#facet:&productBeginIndex:96&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:24&',
        ]
 
        self.pet = 'dog'
        self.type_goods = 'dry food'
        for url in dog_goods:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
 
 
 
 
    def parse(self, response):
        page = response.url.split("/")[-2]
        product_blocks = response.css('div.prod-tile')
        print(len(product_blocks))
        for block in product_blocks:
            try:
                name = block.xpath('.//div[@class="product-name"]/a/span/text()').extract()
                manufacturer  = block.xpath('.//div[@class="product-name"]/a/span/span/text()').extract()
                price = block.xpath('.//span[@class="product-price-promo"]/text()').extract()
                print('PRICE', price[0].rstrip().split("$")[1])
                price = float(price[0].rstrip().split("$")[1])
                name = name[1].rstrip()
                manufacturer = manufacturer[0]
                data = {
                    'pet': self.pet,
                    'type goods': self.type_goods,
                    'manufacturer': manufacturer,
                    'name': name,
                    'price': price
                }
                print(data)
            except Exception as e: 
                print('EXCEPTION', e)