'''
/**
 * Returns the sample variance of a data sequence.
 * That is <tt>(sumOfSquares - mean*sum) / (size - 1)</tt> with <tt>mean = sum/size</tt>.
 *
 * @param size the number of elements of the data sequence. 
 * @param sum <tt>== Sum( data[i] )</tt>.
 * @param sumOfSquares <tt>== Sum( data[i]*data[i] )</tt>.
 */
public static double sampleVariance(int size, double sum, double sumOfSquares) {
	double mean = sum / size;
	return (sumOfSquares - mean*sum) / (size - 1);
}
'''

def sampleVariance(data):

    elements = data.copy()
    size = len(elements)
    suma = 0
    sum = 0

    if(size == 0):
        raise NameError('IligalArgumentException')

    for i in range(0, len(elements)):
        sum += elements[i]

    mean = sum/size

    for i in range(size,-1):
        delta = elements[i] - mean
        suma += delta * delta

    return suma / (size - 1)
