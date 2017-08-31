import regTrees
import numpy as np
# testMat = np.mat(np.eye(4))
# print(testMat)
# mat0, mat1 = regTrees.binSplitDataSet(testMat,1,0.5)
# print(mat0)
# print(mat1)

# myDat = regTrees.loadDataSet('ex00.txt')
# myDat = regTrees.loadDataSet('ex0.txt')
myDat = regTrees.loadDataSet('ex2.txt')
# # print(myDat)
myMat = np.mat(myDat)
# print(regTrees.createTree(myMat))

#后剪枝
myTree = regTrees.createTree(myMat, ops=(0,1))
myDatTest = regTrees.loadDataSet('ex2test.txt')
myMat2Test = np.mat(myDatTest)
regTrees.prune(myTree,myMat2Test)

