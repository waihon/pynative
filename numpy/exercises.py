import numpy

firstArray = numpy.empty([4, 2], dtype = numpy.float64)
print(firstArray)
print(firstArray.shape)
print(firstArray.ndim)
print(firstArray.itemsize)

secondArray = numpy.arange(100, 200, 10)
secondArray = secondArray.reshape(5, 2)
print(secondArray)

thirdArray = numpy.array(
    [
        [11, 22, 33],
        [44, 55, 66],
        [77, 88, 99]
    ]
)
print(thirdArray)
print(thirdArray[..., 2])

forthArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print(forthArray)
print(forthArray[0::2, 1::2])
