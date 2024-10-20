import numpy

sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8, 3)
print(sampleArray)

subArrays = numpy.split(sampleArray, 4)
print(subArrays)
