import operator
import os
from numpy import *

def createDataSet():
    group = array([[100.0,1.1], [98.0,1.0], [0,1000], [1.0,998]])
    labels = ['A','A','B','B']
    return group, labels

def read2matrix(filename):
    f_handle = open(filename)
    arrayOfLines = f_handle.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        # 每个样本有3个特征
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        # listFromLine[-1]放的是样本的label
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

def autoNorm(dataSet):
    # new_value = (oldValue-min) / (max-min)
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    # 生成一个0矩阵
    normDataSet = zeros(shape(dataSet))
    # m为样本的维度
    m = dataSet.shape[0]
    # 将所有样本值和最小值相减
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet / tile(ranges, (m,1))
    return normDataSet, ranges, minVals

