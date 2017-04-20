import operator
from math import log

def calcShannoEnt(dataSet):
    dataSize = len(dataSet)
    labelCounts = {}
    for item in dataSet:
        currentLabel = item[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / dataSize
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]

    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for item in dataSet:
        if item[axis] == value:
            reduceFeatVec = item[:axis]
            reduceFeatVec.extend(item[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannoEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = -1;
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            # 保留并去掉第i项特征等于value的样本，并计算去除后的熵
            subDataSet = splitDataSet(dataSet, i, value)
            # 计算第i项等于value的概率
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannoEnt(subDataSet)
        # 求熵增益
        infoGain = baseEntropy - newEntropy
        # 找出熵增益最小的项
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),
                              reverse=True)
    return sortedClassCount

def createTree(dataSet, labels):
    classList = [item[-1] for item in dataSet]
    # 如果只有完全相同的分离，停止划分
    if classList.count(classList[0]) == len(dataSet):
        return classList[0]
    # 每个样本只有一个特征项的情况
    if len(dataSet[0]) == 1:
        # 之间可以按类区分
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeatLabel]
    myTree = {bestFeat: {}}
    del(labels[bestFeat])
    featValues = [item[bestFeat] for item in dataSet]
    unniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels
        # 保留但去除值为value的项
        subData = splitDataSet(dataSet, bestFeat, value)
        myTree[bestFeatLabel] = createTree(subData, subLabels)
    return myTree

def main():
    dataSet, labels = createDataSet()
    print(calcShannoEnt(dataSet))
    print(chooseBestFeatureToSplit(dataSet))

main()
