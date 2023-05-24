def harmonicMean(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        if data[i] == 0:
            return 'd/0'	
        else:
            sumOfInversions += 1 / data[i]

    if sumOfInversions == 0:
        return 'd/0'
    else:
        return len(data) / sumOfInversions


