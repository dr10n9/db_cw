import pymongo
from pymongo import ReadPreference
import re

connection = pymongo.MongoClient('localhost:27010')
db = connection.get_database('cw', read_preference=ReadPreference.SECONDARY)

# connection = pymongo.MongoClient([
#     'localhost:27017',
#     'localhost:27018',
#     'localhost:27019'
# ],replicaset='replica1')

# db = connection.get_database('test', read_preference=ReadPreference.SECONDARY)

def get_by_manufacturer(manufacturer='', source=''):
    return db.guitars.find({
        'manufacturer': re.compile(manufacturer, re.IGNORECASE),
        'source': source
    })

def get_in_price_range(min_price=0, max_price = 1000000, manufacturer='', model='', source=None):
    res = db.guitars.find({
        'price': {
            '$gt': min_price,
            '$lt': max_price
        },
        'source': source,
        'manufacturer': re.compile(manufacturer, re.IGNORECASE),
        'model': re.compile(r'{0}'.format(model), re.I)
    }).sort('price', 1)
    return res

# thomann = len(list(get_by_manufacturer('fender', 'thomann')))
# muztorg = len(list(get_by_manufacturer('fender', 'muztorg')))

# print(f't: {thomann} | m: {muztorg}')

def get_average_shipping(data):
    average = 0
    for d in data:
        average += d['shipping']
    ret = 0
    try:
        ret = round(average/data.count(), 2)
    except Exception as e:
        print(e)
    return ret

def shipping_price_in_region(region=''):
    data = db.reverb.find({'region': region})
    return get_average_shipping(data)

def shipping_price_by_manufactuer(manufacturer=''):
    data = db.reverb.find({
        'manufacturer': re.compile(manufacturer, re.IGNORECASE),
    })
    return get_average_shipping(data)
    

def shipping_price_by_manufactuer_and_region(manufacturer='', region=''):
    return get_average_shipping(
        db.reverb.find({
            'manufacturer': re.compile(manufacturer, re.IGNORECASE),
            'region': region
        })
    )

def shipping_price():
    item_regions = ['FR', 'JP', 'US', 'CA', 'RU', 'MX', 'PL', 'IT', 'DE', 'ES', 'BE', 'NL', 'CN']
    manufacturers = ['ibanez', 'gibson', 'epiphone', 'fender']
    for m in manufacturers:
        for r in item_regions:
            try:
                print(f'{m} from {r}: {shipping_price_by_manufactuer_and_region(m, r)}')
            except Exception as e:
                print(e)
    # for region in item_regions:
    #     try:
    #         print(f'average shipping price from {region}: {round(shipping_price_in_region(region), 2)}')
    #     except Exception as e:
    #         print(e)

if __name__ == "__main__":
    shipping_price()


# manufacturer = 'fender'
# model = 'strat'
# min_price = 0
# max_price = 5000

# print('thomann\n')

# middle1 = 0
# middle2 = 0
# counter = 0

# for item in get_in_price_range(
#         min_price=min_price, max_price=max_price, manufacturer=manufacturer, model=model, source='thomann'
#     ):
#     middle1 += item.get('price')
#     counter += 1
#     print(item)
# middle1 = middle1/counter

# print('\nmuztorg\n')
# counter = 0
# for item in get_in_price_range(
#         min_price=min_price, max_price=max_price, manufacturer=manufacturer, model=model, source='muztorg'
#     ):
#     print(item)
#     middle2 += item.get('price')
#     counter += 1
# middle2 = middle2/counter

# print(f'thomann: {middle1}\nmuztorg: {middle2}\npercentage: {100 - middle1/middle2 * 100}')

# db.guitars.drop()
