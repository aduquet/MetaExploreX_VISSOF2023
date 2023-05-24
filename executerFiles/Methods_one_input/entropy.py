import numpy as np


def entropy(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    if sum_k == 0:
        return 'd/0'
    else:
        for i in k:
            if i != 0:
                p_i = i / sum_k
                h += p_i * np.log(p_i)

        return -h
