def find_median(a):
    # k = len(a) / 2 + 1
    # minIndex = 0
    # minValue = a[0]
    # for i in range(0, k):
    #     minIndex = i
    #     minValue = a[i]

    #     for j in range(i + 1, len(a)):
    #         if a[j] < minValue:
    #             minIndex = j
    #             minValue = a[j]

    #     temp = a[i]
    #     a[i] = a[minIndex]
    #     a[minIndex] = temp
    # if len(a) % 2 == 0:
    #     return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    # else:
    #     return a[len(a)/2]

    # sorting the list
    a.sort()
    # finding the median
    n = len(a)
    if n % 2 == 0:
        median = (a[n//2 - 1] + a[n//2]) / 2
    else:
        median = a[n//2]

    return median
