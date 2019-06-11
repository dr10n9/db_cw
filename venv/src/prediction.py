from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.datasets.samples_generator import make_blobs
from sklearn import linear_model, preprocessing
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import filter


def linear_regression_prediction(price=100, step=25, plus_step=100):
    # model = linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
    # model = preprocessing.PolynomialFeatures(2, include_bias=False)
    # model = linear_model.LinearRegression()
    prices = []
    percentage = []

    below = []
    for i in range(0, 4000, step):
        muztorg = filter.get_in_price_range(i, i+plus_step+step, source='muztorg')
        thomann = filter.get_in_price_range(i, i+plus_step+step, source='thomann')
        t_a = 0
        m_a = 0
        for t in thomann:
            t_a += t['price']
        for m in muztorg:
            m_a += m['price']
        try:
            t_a = t_a/thomann.count()
            m_a = m_a/muztorg.count()  
            p = (m_a/t_a - 1)*100
            if p < 0:
                print(i, ': ', p)
                below.append(i)
            percentage.append(p)
            prices.append([i])
        except Exception as e:
            """"""
            # print(e)
    poly = PolynomialFeatures(8, include_bias=True)

    X = np.array(prices).reshape(-1, 1)

    X_poly = poly.fit_transform(X)
    linear = LinearRegression()
    linear.fit(X_poly, percentage)
    y_1 = []
    y_2 = []
    x = []
    for i in range(0,4000,100):
        x.append(i)
        y_1.append(i)
        y_2.append(i + i * linear.predict(poly.fit_transform([[i]])))
    import matplotlib.pyplot as plt
    plt.plot(x, y_1, label='thomann')
    plt.plot(x, y_2, label='predicted')
    plt.title('prediction')
    plt.legend()
    plt.savefig('prediction.png')
    plt.close()

linear_regression_prediction()
    # plot.plot()
    # res = linear.predict(poly.fit_transform([[price]]))


    # print('x:\n', prices, '\ny:\n', percentage) 
    # 
    #

    # for j in range(25): 
    #     print('\n\n\ndegrees: ', j)     
    #     poly = PolynomialFeatures(j, include_bias=True)

    #     X = np.array(prices).reshape(-1, 1)

    #     X_poly = poly.fit_transform(X)
    #     linear = LinearRegression()
    #     linear.fit(X_poly, percentage)
    #     res = linear.predict(poly.fit_transform([[price]]))
    #     print('RESULTS\n')
    #     f = open(f'prediction/d{j}', 'w')
    #     for i in range(0, 4000, 100):
    #         res = linear.predict(poly.fit_transform([[i]]))
    #         f.write(f'{i} (EU) : {i*res[0]+i} (UA)\n')
    #     f.close()


# prices = []
# for i in range(0, 5000, 250):
#     prices.append(f'{i} (UA): {linear_regression_prediction(i)} (UA)')

# for p in prices:
#     print(p)
linear_regression_prediction(1000)
    # model.fit(prices, percentage)
    # print(len(prices), len(percentage))
    # prices = np.linspace(prices, stop=10000,endpoint=False, num=len(prices))
    # print(len(prices))
    # x_new = np.hstack([prices**2])
    # samples, nx, ny = x_new.shape
    # d2_prices = x_new.reshape((samples,nx*ny))

    # print(x_new.shape)
    # print(x_new)
    # model.fit(d2_prices, percentage)
    # print(model.predict([[1000]]))

# linear_regression_prediction(step=100)

def polynomial():
    step = 300
    prices = []
    percentage = []

    for i in range(0, 5000, step):
        muztorg = filter.get_in_price_range(i, i+plus_step+step, source='muztorg')
        thomann = filter.get_in_price_range(i, i+plus_step+step, source='thomann')
        t_a = 0
        m_a = 0
        for t in thomann:
            t_a += t['price']
        for m in muztorg:
            m_a += m['price']
        try:
            t_a = t_a/thomann.count()
            m_a = m_a/muztorg.count()  
            p = (m_a/t_a - 1)*100
            if p < 0:
                print(i, ': ', p)
                below.append(i)
            percentage.append(p)
            prices.append([i])
        except Exception as e:
            """"""
    # model = preprocessing.PolynomialFeatures(4, include_bias=True)
# linear_regression_prediction(step=300)
# print(linear_regression_prediction(250, step=10))
# print(linear_regression_prediction(1500))

# step = 300
# max_price = 5000
# y = []
# x = []
# for i in range(0, 5000, step):
#     muztorg = filter.get_in_price_range(i, i+step, source='muztorg')
#     thomann = filter.get_in_price_range(i, i+step, source='thomann')
#     t_a = 0
#     m_a = 0
#     for t in thomann:
#         t_a += t['price']
#     for m in muztorg:
#         m_a += m['price']
#     try:
#         t_a = t_a/thomann.count()
#         m_a = m_a/muztorg.count()
        
#         y.append((m_a/t_a - 1)*100)
#         # y.append(((m_a/muztorg.count())/(t_a/thomann.count())))
#         x.append(i)
#     except Exception as e:
#         print(e)
    
# model = LogisticRegression()
# model.fit(x, y)

# Xnew, _ = make_blobs(n_samples=20, centers=2, n_features=2, random_state=1)
# ynew = model.predict(Xnew)
# # show the inputs and predicted outputs
# for i in range(len(Xnew)):
#     print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))


# # generate 2d classification dataset
# X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
# # fit final model
# print(X, y)
# model = LogisticRegression()
# model.fit(X, y)
# # new instances where we do not know the answer
# Xnew, _ = make_blobs(n_samples=20, centers=2, n_features=2, random_state=1)
# # make a prediction
# ynew = model.predict(Xnew)
# # show the inputs and predicted outputs
# # for i in range(len(Xnew)):
# # 	print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
