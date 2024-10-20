import numpy

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print(sampleArray)

# Delete 2nd column
sampleArray = numpy.delete(sampleArray, 1, axis = 0)
print(sampleArray)

# Insert a new column as 2nd column
newColumn = numpy.array([[10,10,10]])
sampleArray = numpy.insert(sampleArray, 1, newColumn, axis = 0)
print(sampleArray)
