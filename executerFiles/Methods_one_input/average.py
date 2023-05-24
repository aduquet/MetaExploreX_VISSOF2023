def average(a):
    if(len(a) == 0):
        return -111111
    else:
        sum = 0
        for i in a:
            sum += i
        return sum/len(a)