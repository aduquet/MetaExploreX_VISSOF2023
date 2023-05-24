#  (Reverse an array) 

def reverse(a):
    r = []
    cnt = 0

    for i in range(len(a), -1):
        r.append(a[i])

    return r
