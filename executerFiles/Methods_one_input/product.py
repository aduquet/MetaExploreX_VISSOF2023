'''
/**
 * Returns the product of a data sequence, which is <tt>Prod( data[i] )</tt>.
 * In other words: <tt>data[0]*data[1]*...*data[data.size()-1]</tt>.
 * Note that you may easily get numeric overflows.
 */
public static double product(DoubleArrayList data) {
	int size = data.size();
	double[] elements = data.elements();
	
	double product = 1;
	for (int i=size; --i >= 0;) product *= elements[i];
	
	return product;
}
'''
def product(data):

    size = len(data)
    elements = data.copy()
    product = 1
    

    for i in range(size - 1, -1, -1):
        if(elements[i] == 'N/A'):
            return 'd/0'
        product *= elements[i]

    return product
