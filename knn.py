# from https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator

def loadDataset(filename, split, trainingSet=[], testSet=[]):
    """Loads a data set.

    >>> trainingSet = []
    >>> testSet = []
    >>> loadDataset('iris.csv', 0.66, trainingSet, testSet)
    """
    with open('iris.csv', 'r') as datafile:
        lines = csv.reader(datafile)
        dataset = list(lines)
        for i in range(len(dataset)-1):
            for j in range(4):
                dataset[i][j] = float(dataset[i][j])
            if random.random() < split:
                trainingSet.append(dataset[i])
            else:
                testSet.append(dataset[i])

def euclideanDistance(instance1, instance2, length):
    """Computes the euclidean distance between two data points.
    
    >>> data1 = [2, 2, 2, 'a']
    >>> data2 = [4, 4, 4, 'b']
    >>> distance = euclideanDistance(data1, data2, 3)
    >>> print('Distance: ' + repr(distance))
    Distance: 2.0
    """
    distance = 0
    for j in range(length):
        distance += pow((instance1[j] - instance2[j]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    """Gets the k closest neighbors for a test instance

    >>> trainingSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
    >>> testInstance = [5, 5, 5]
    >>> k = 1
    >>> neighbors = getNeighbors(trainingSet, testInstance, k)
    >>> print(neighbors)
    [[4, 4, 4, 'b']]
    """
    distances = []
    length = len(testInstance) - 1
    for i in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[i], length)
        distances.append((trainingSet[i], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def getResponse(neighbors):
    """Gets the most frequent class from the neighbors. 

    The class should be the last attribute of each neighbor.
    >>> neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
    >>> response = getResponse(neighbors)
    >>> print(response)
    a
    """
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    """Gets the accuracy of the predictions.

    >>> testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
    >>> predictions = ['a', 'a', 'a']
    >>> accuracy = getAccuracy(testSet, predictions)
    >>> print('{:.2%}'.format(accuracy))
    66.67%
    """
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct / float(len(testSet)))

def main():

    # perpare data
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset('iris.csv', split, trainingSet, testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))

    # generate predictions
    predictions = []
    k = 5
    for i in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[i], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[i]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: {:.2%}'.format(accuracy))

import doctest
doctest.testmod()

main()
