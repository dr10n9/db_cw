import scrapy

class zootovary(scrapy.Spider):
    name = 'zootovary'
    def start_requests(self):
        links = [
            'https://www.zootovary.com/Dog-home-c-22.html'
        ]

        accesories = [

        ]

        vitamines = [

        ]

        dry_food = [
            
        ]

        for link in links:
            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        product_blocks = response.css('div.feaBox')
        print(len(product_blocks))
        for block in product_blocks:
            name = block.xpath('.//div[@class="nameHP"]/a/text()').extract()[0]
            price = block.xpath('.//div[@class="priceHP"]/b/nobr/text()').extract()
            if len(price) == 0:
                price = block.xpath('.//div[@class="priceHP"]/b/text()').extract()
            price = price[0].split(',')
            price = ''.join(price)
            price = price.split(' ')
            tmp = price
            for p in tmp:
                try:
                    price = float(p)
                except Exception as e:
                    """"""
                    # print(e)
            data = {
                'name': name,
                'price': price
            }
            print(data)
