

# import matplotlib
# import matplotlib.pyplot as plt
# import pymongo
# from pymongo import ReadPreference
# import numpy as np


# import filter

# manufacturer = ''
# model = ''

# connection = pymongo.MongoClient('localhost:27010')
# db = connection.get_database('cw', read_preference=ReadPreference.SECONDARY)

# source = 'thomann'

# total = len(list(db.guitars.find({
#     'source': source
# })))

# max_price = db.guitars.find_one({
#     "source": source
# }, sort=[("price", -1)]).get('price')

# print(max_price)

# step = 500

# amounts = []
# prices = []
# for price in range(0, int(max_price) + 1, step):
#     prices.append(price)
#     cur = db.guitars.find({
#         'price': {
#             '$gt': price,
#             '$lt': price + step
#         },
#         'source': source
#     })
#     cur = len(list(cur))
#     # print(f'cur: {cur} | total : {total}')
#     # print(100 * cur / total)
#     amounts.append(100 * cur / total)

# print(prices)
# print(amounts)

# plt.plot(prices, amounts)
# plt.xlabel('prices')
# plt.ylabel('percentage')
# plt.savefig(f'./{source}_amount.png')


# min_price = 0
# max_price = 5000

# prices = []
# percentage = []
# step = 100

# for price in range(0, 5000, int(step/2)):
#     print(f'range: ({price}, {price + step})')
#     muztorg = filter.get_in_price_range(price, price + step, manufacturer=manufacturer, model=model, source='muztorg')
#     thomann = filter.get_in_price_range(price, price + step, manufacturer=manufacturer, model=model, source='thomann')
   
#     muztorg_average = 0
#     thomann_average = 0
#     counter_m = 0
#     counter_t = 0

#     for item in muztorg:
#         muztorg_average += item.get('price')
#         counter_m += 1


#     counter = 0
#     for item in thomann:
#         thomann_average += item.get('price')
#         counter_t += 1

#     try:
#         muztorg_average = muztorg_average/counter_m
#         thomann_average = thomann_average/counter_t
#         percentage.append(100 - thomann_average/muztorg_average * 100)
#         prices.append(price)
#     except Exception as e:
#         print(e)



# plt.plot(prices, percentage)
# plt.xlabel('prices')
# plt.ylabel('percentage')
# plt.savefig('./1.png')

# plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
# plt.xlabel('Months')
# plt.ylabel('Books Read')
# plt.show
# plt.savefig('./1.png')
# matplotlib.pyplot.savefig()
# plt.show()
# plt.savefig('books_read.png')