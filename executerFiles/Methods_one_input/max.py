'''
/**
 * Returns the largest member of a data sequence.
 */
public static double max(DoubleArrayList data) {
	int size = data.size();
	if (size==0) throw new IllegalArgumentException();
	
	double[] elements = data.elements();
	double max = elements[size-1];
	for (int i = size-1; --i >= 0;) {
		if (elements[i] > max) max = elements[i];
	}

	return max;
}
'''

def max(data):
    size = len(data)
    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()

    mix = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] > mix:
            mix = elements[i]

    return mix
