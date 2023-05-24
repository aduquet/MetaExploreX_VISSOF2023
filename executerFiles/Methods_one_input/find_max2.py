# (maximum value of addition of two consecutive elements in an array)

def find_max2(a):

    max1 = a[0] + a[1]

    for i in range(1, len(a) - 1):
        if a[i] + a[i + 1] > max1:
            max1 = a[i] + a[i + 1]

    return max1
