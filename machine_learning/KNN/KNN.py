import operator
import os
import matplotlib
import matplotlib.pyplot as plt
from numpy import *
from data_collector import createDataSet
from data_collector import read2matrix
from data_collector import autoNorm
from image_processing import formatTrainingData1
from image_processing import formatTestingData1

def classify0(inX, dataSet, labels, k):
    # inX 输入向量
    # dataSet 为训练样本

    dataSetSize = dataSet.shape[0]
    # 计算输入向量与训练样本的差值
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 差值的平方
    sqDiffMat = diffMat**2
    # 计算两坐标的平方和得到向量的距离
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    # 按距离的大小排序,
    # 因为distances由很多一维的数据组成
    # 所以sort后得到的是这些数据的索引值,也就是labels的标签号
    # 注:argsort()的用法
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),
                              reverse=True)
    return sortedClassCount[0][0]

def numberClassTest():
    fileDir = '/Users/leung/test_file/test_room/digits'
    group, labels = formatTrainingData1(fileDir)
    testFileList = os.listdir('%s/testDigits' % fileDir)
    errorCount = 0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        vectorUnderTest, classNumStr = formatTestingData1(fileDir, fileNameStr)
        classifierResult = classify0(vectorUnderTest,
                                     group, labels, 5)
        print("machine answer: %s, the real answer: %s"% (classifierResult, classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1
    print("total error: %d" % errorCount)
    print("error rate: %f" % (errorCount/mTest))
    return group, labels
    
def main():
    # group, labels = createDataSet()
    # group = autoNorm(group)[0]
    group, labels = numberClassTest() 
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(group[:,0], group[:,1])
    # plt.show()
    # print(classify0([100,100], group, labels, 3))

main()
