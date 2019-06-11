import random as rnd
import datetime as dt

def change_price(price):
    decision = rnd.randint(-1, 1)
    if decision == -1:
        print('make lower')
        return price - price * rnd.randint(5, 10)/100
    elif decision == 1:
        print('make higher')
        return price + price * rnd.randint(5, 10)/100
    elif decision == 0:
        print('no change')

# months = dict()

def generate(obj):
    print("!!!!!!", obj)
    current = dt.datetime.now()
    current = dt.date(current.year, current.month, current.day)
    begin_m = current.month - 5
    day = 1
    # print(begin_m)
    new_date = dt.date(current.year, begin_m, day)
    while new_date < current:
        tmp = obj
        tmp['date'] = new_date
        tmp['price'] = change_price(tmp['price'])
        day += 7
        if day > 28:
            begin_m += 1
            day = (31 - day) % 7
        new_date = dt.date(current.year, begin_m, day)
        print(tmp)
        # TODO
        # save in database    

def get_date(obj):
    date_arr = obj['date'].split('-')
    return dt.date(date_arr[0], date_arr[1], date_arr[2])

tmp = dict()
tmp['price'] = float(125.00)
print(tmp)

generate(tmp)


