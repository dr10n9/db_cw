import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import filter

def autolabel(rects, xpos='center', ax=None):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

def amount_by_manufacturers():
    manufacturer_names = [
        'fender',
        'gibson',
        'epiphone',
        'ibanez',
        'esp',
        'chapman'
    ]

    muztorg = []
    thomann = []
    muztorg_std = (1, 2, 3, 4, 5, 6)
    thomann_std = (1, 2, 3, 4, 5, 6)

    for name in manufacturer_names:
        muztorg.append(len(list(filter.get_by_manufacturer(name, 'muztorg'))))
        thomann.append(len(list(filter.get_by_manufacturer(name, 'thomann'))))

    
    fig, ax = plt.subplots()
    ind = np.arange(len(muztorg))
    width = 0.35

    rects1 = ax.bar(ind - width/2, muztorg, width, yerr=muztorg_std, label='muztorg')
    rects2 = ax.bar(ind + width/2, thomann, width, yerr=thomann_std, label='thomann')


    ax.set_ylabel('Amount')
    ax.set_xlabel('Manufacturers')
    ax.set_xticks(ind)
    ax.set_xticklabels(manufacturer_names)
    ax.legend()

    autolabel(rects1, "left", ax=ax)
    autolabel(rects2, "right", ax=ax)
    fig.tight_layout()
    plt.savefig("results/manufacturers_amount.png")


def amount_by_price_range(max_price=1000, step=100):
    prices = []
    muztorg = []
    thomann = []
    muztorg_std = (1, 2, 3, 4, 5, 6)
    thomann_std = (1, 2, 3, 4, 5, 6)

    for i in range(0, max_price, step):
        prices.append(f'{i}-{i+step}')
        muztorg.append(len(list(filter.get_in_price_range(i, i+step, source='muztorg'))))
        thomann.append(len(list(filter.get_in_price_range(i, i+step, source='thomann'))))
        fig, ax = plt.subplots()
    
    print(f'm: {muztorg} | t: {thomann}')
    ind = np.arange(len(muztorg))
    width = 0.35

    rects1 = ax.bar(ind - width/2, muztorg, width, label='muztorg')
    rects2 = ax.bar(ind + width/2, thomann, width, label='thomann')


    ax.set_ylabel('Amount')
    ax.set_xlabel("Price range")
    ax.set_xticks(ind)
    ax.set_xticklabels(prices)
    ax.legend()

    autolabel(rects1, "left", ax=ax)
    autolabel(rects2, "right", ax=ax)
    fig.tight_layout()
    plt.savefig("results/prices_amount.png")


amount_by_manufacturers()
amount_by_price_range(5000, 1000)