def count_non_zeros(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt

def add_values(data):

    sum = 0
    for i in data:
        sum += i
    return sum
