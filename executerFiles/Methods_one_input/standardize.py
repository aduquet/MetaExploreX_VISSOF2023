'''
/**
 * Modifies a data sequence to be standardized.
 * Changes each element <tt>data[i]</tt> as follows: <tt>data[i] = (data[i]-mean)/standardDeviation</tt>.
 */
public static void standardize(DoubleArrayList data, double mean, double standardDeviation) {
	double[] elements = data.elements();
	for (int i=data.size(); --i >= 0;) elements[i] = (elements[i]-mean)/standardDeviation;
}
'''

import math


def standardize(data):
    suma = 0
    sumSq = 0

    try:

        for i in range(0, len(data)):
            suma += data[i]
            sumSq += data[i] * data[i]

        mean = suma / len(data)
        sd = math.sqrt((sumSq - mean * suma) / len(data))

        for i in range(0, len(data)):
            data[i] = (data[i] - mean) / sd

        return data
    
    except:
        return -11111
