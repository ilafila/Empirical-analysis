import random
import time
import matplotlib.pyplot as plt

def generator(size):
    return [random.randint(-510, 510) for i in range(size)]

def swap(array, firstElement, secondElement):
    tmp = array[firstElement]
    array[firstElement] = array[secondElement]
    array[secondElement] = tmp

def partition(array, start, length):
    i = start
    j = start
    while j < length - 1:
        if (array[j] <= array[length - 1]):
            swap(array, i, j)
            i += 1
        j += 1
    swap(array, i, j)
    return i

def quickSort(array, left, length):
    if (left + 1 >= length):
        return
    pivotIndexStart = random.randint(left, length - 1)
    swap(array, pivotIndexStart, length - 1)
    pivotIndex = partition(array, left, length)
    quickSort(array, left, pivotIndex)
    quickSort(array, pivotIndex + 1, length)

def experiment():
    times = []
    dots = []
    for k in range(10, 10000, 20):
        timesSum = 0
        countsOfExperiments = 20
        for i in range(countsOfExperiments):
            testArray = generator(k)
            startTime = time.time()
            quickSort(testArray, 0, len(testArray))
            timesSum += time.time() - startTime
        middleTime = timesSum / countsOfExperiments
        dots.append(k)
        times.append(middleTime)
        print(k, ': ', '{:.5f}'.format(middleTime), end='\n')
    plt.scatter(dots, times, c='b')
    plt.show()

experiment()
