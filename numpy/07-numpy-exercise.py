import numpy

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

# Sorting original array by 2nd row
print(sampleArray[1,:].argsort())
sortedArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]
print(sortedArrayByRow)

# Sorting original array by 2nd column
print(sampleArray[:,1].argsort())
sortedArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortedArrayByColumn)
