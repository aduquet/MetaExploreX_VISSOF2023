'''
Returns the smallest member of a data sequence.

JAVA VERSION
public static double min(DoubleArrayList data) {
	int size = data.size();
	if (size==0) throw new IllegalArgumentException();
	
	double[] elements = data.elements();
	double min = elements[size-1];
	for (int i = size-1; --i >= 0;) {
		if (elements[i] < min) min = elements[i];
	}

	return min;
}'''

def min(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    min = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min