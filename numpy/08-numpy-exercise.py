import numpy

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

# Axis 0 = X (Column)
minOfAxisZero = numpy.amin(sampleArray, 0)
print(minOfAxisZero)
maxOfAxisZero = numpy.amax(sampleArray, 0)
print(maxOfAxisZero)

# Axis 1 = Y (Row)
minOfAxisOne = numpy.amin(sampleArray, 1)
print(minOfAxisOne)
maxOfAxisOne = numpy.amax(sampleArray, 1)
print(maxOfAxisOne)
