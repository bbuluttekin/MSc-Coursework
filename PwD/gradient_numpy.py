# Input data and give us a function!

import numpy as np
import sys


def grad_desc(x, y, l_rate=0.00001, limit_err=0.001):
    # Looking for y = m*x + b => (I know that it should be y = 2x+3)
    results = []
    converged = False
    m, b = 0, 0
    count = 0
    n = len(x)
    learning_rate = l_rate

    e = sys.maxsize  # Maxsize intiger of python
    iter = 10000
    limit_error = limit_err
    while not converged:
        count += 1
        y_predicted = m * x + b
        mse = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m = m - learning_rate * md
        b = b - learning_rate * bd

        if abs(mse - e) <= limit_error:
            converged = True
        if iter == count:
            converged = True
        e = mse
        print("f(x) =  {}* x + {}, with mse {}, iteration {}".format(m, b, mse, count))

    results.append([count, m, b, mse])
    print("f(x) =  {}* x + {}, with mse {} after iteration {}".format(round(m),
                                                                      round(b, 0), round(mse, 5), count))
    return mse


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])


min_mse = {}
for i in [0.01, 0.001, 0.0001, 0.000001]:
    min_mse[grad_desc(x, y, limit_err=i)] = i

print("Result:")
print(min_mse[min(min_mse.keys())])
