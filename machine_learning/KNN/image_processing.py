import numpy
import os
from numpy import *

def img2vector(filename):
    returnVect = zeros((1,1024))
    file_handle = open(filename)
    for i in range(32):
        lineStr = file_handle.readline()
        for j in range(32):
            returnVect[0, 32*i + j] = int(lineStr[j])
    return returnVect

def formatTrainingData1(fileDir):
    labels = []
    trainingFileDir = '%s/trainingDigits' % fileDir
    trainingFileList = os.listdir(trainingFileDir)
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        labels.append(classNumStr)
        trainingMat[i, :] = img2vector('%s/%s' % (trainingFileDir, fileNameStr))
    return trainingMat, labels

def formatTestingData1(fileDir, fileNameStr):
    # testFileList = os.listdir('%s/testDigits' % testFileDir)
    # errorCount = 0
    # mTest = len(testFileList)
    # for i in range(mTest):
        # fileNameStr = testFileList[i]
    testFileDir = '%s/testDigits' % fileDir
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    vectorUnderTest = img2vector('%s/%s' % (testFileDir, fileNameStr))
    return vectorUnderTest, classNumStr
    
