import requests
import json
import os   
import time

import pymongo
from pymongo import ReadPreference

connection = pymongo.MongoClient("localhost:27010")
db = connection.get_database('cw', read_preference=ReadPreference.SECONDARY)


TOKEN = 'c1a5c9732610ed9b707a740e3136d14df768be1965fbf8d2fc8a2e67ba05a927'
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept-Version": "3.0"
}
print(headers)

item_regions = ['FR', 'JP', 'US', 'CA', 'RU', 'MX', 'PL', 'IT', 'DE', 'ES', 'BE', 'NL', 'CN']
# item_regions = ['FR']

ON_PAGE = 50
LIMIT = 7000

more_than_100 = 0
less_than_100 = 0
ua = 0
average = 0

total = 0
total_pages = 0
current_page = 0

region_quantity = dict()

os.system('clear')
print('sending request to get quantity of items')
for region in item_regions:
    res = requests.get(
        f'https://api.reverb.com/api/listings?ships_to=UA&category=electric-guitars&item_region={region}&page=1&per_page={ON_PAGE}',
        headers=headers
    ).json()
    region_quantity[region] = res['total']

print('DONE')
for key in region_quantity.keys():
    print(f'{key}: {int(region_quantity[key]/ON_PAGE)}')
    total += region_quantity[key]
total_pages = int(total/ON_PAGE)
print(f'Total instruments: {total}')
time.sleep(1)
os.system('clear')

def process_url(url):
    res = requests.get(
        url,
        headers=headers
    ).json()
    if 'message' in res:
        print(res)
    else:
        if 'listings' in res:
            for r in res['listings']:
                if 'shipping' in r:
                    shipping = r['shipping']
                    shipping_price = 0
                    if 'rates' in shipping:
                        for rate in shipping['rates']:
                            if rate['region_code'] == 'XX':
                                shipping_price = rate['rate']['amount_cents'] / 100
                            if rate['region_code'] == 'UA':
                                shipping_price = rate['rate']['amount_cents'] / 100
                                break
                        to_save = {
                            "region": key,
                            "manufacturer": r['make'],
                            "model": r['model'],
                            "price": r['price']['amount'],
                            "shipping": shipping_price
                        }
                        db.reverb.insert_one(to_save)    
                    
        else:
            """"""

total_pages_processed = 0

for i in range(400):
    url = f'https://api.reverb.com/api/listings?ships_to=UA&category=electric-guitars&item_region=US&page={i}&per_page={ON_PAGE}'
    key = 'US'
    process_url(url)
    os.system('clear')
    print(f'{i}/400 ({round(i/400, 4) * 100}%)\nprocessing {url}')

# start = time.time()


for key in region_quantity.keys():
    pages = int(region_quantity[key]/ON_PAGE)
    print(f'{key}: {pages}')
    api_limiter = 0
    if pages > 400:
        api_limiter = 400
    else:
        api_limiter = pages
    for i in range(1, api_limiter, 1):
        url = f'https://api.reverb.com/api/listings?ships_to=UA&category=electric-guitars&item_region={key}&page={i}&per_page={ON_PAGE}'
        process_url(url)
        total_pages_processed += 1
        # print()
        os.system('clear')
        print(f'processing {i}/{api_limiter} in key={key}')
        print(f'processing {url}')
        cur = time.time()
        time_spent = time.strftime('%H:%M:%S', time.gmtime(cur - start))
        print(f'pages processed: {total_pages_processed}; time spent: {time_spent}')


# start = time.time()
# for key in region_quantity.keys():
#     pages = int(region_quantity[key]/ON_PAGE)
#     print(pages)
#     for i in range(850, pages):
#         url = f'https://api.reverb.com/api/listings?ships_to=UA&category=electric-guitars&item_region={key}&page={i}&per_page={ON_PAGE}'
#         print(url)
#         res = requests.get(
#             url,
#             headers=headers
#         ).json()
#         print(res)
#         if 'listings' in res:
#             for r in res['listings']:
#                 if 'shipping' in r:
#                     shipping = r['shipping']
#                     shipping_price = 0
#                     if 'rates' in shipping:
#                         for rate in shipping['rates']:
#                             ua_flag = False
#                             if rate['region_code'] == 'XX' and not ua_flag:
#                                 shipping_price = rate['rate']['amount_cents'] / 100
#                             if rate['region_code'] == 'UA':
#                                 shipping_price = rate['rate']['amount_cents'] / 100
#                                 ua_flag = True
#                                 break
#                                 # TODO save obj in database
#                         to_save = {
#                             "region": key,
#                             "manufacturer": r['make'],
#                             "model": r['model'],
#                             "price": r['price']['amount'],
#                             "shipping": shipping_price
#                         }
#                         db.reverb.insert_one(to_save)
#                     else:
#                         print('no rates in shipping')
#                 else: 
#                     print('no shipping in r')
#                     # print(to_save)  
#             end = time.time()
#             os.system('clear')
#             current_page += 1
#             print(f'{current_page}/{total_pages} ({round(current_page/total_pages, 4) * 100}%) processed')
#             time_spent = round(end - start)
#             print(f'processing {url}')
#             est = time.strftime('%H:%M:%S', time.gmtime(round((time_spent)/(current_page+1) * total_pages - (time_spent))))
#             time_spent = time.strftime('%H:%M:%S', time.gmtime(time_spent))
#             print(f'spent: {time_spent} | est: {est}')
#         else:
#             print(f'no listing in res: {i}')
#             break
