import math


def geometric_mean(data):
    product = 1
    try:
        for i in data:
            product *= i

        return math.pow(product, 1/len(data))
    except:

        return 'd/0'