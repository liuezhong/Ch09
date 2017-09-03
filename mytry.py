import regTrees
import numpy as np
# testMat = np.mat(np.eye(4))
# print(testMat)
# mat0, mat1 = regTrees.binSplitDataSet(testMat,1,0.5)
# print(mat0)
# print(mat1)

# myDat = regTrees.loadDataSet('ex00.txt')
# myDat = regTrees.loadDataSet('ex0.txt')

# print(myDat)
# myMat = np.mat(myDat)
# print(regTrees.createTree(myMat))

#后剪枝
# myDat = regTrees.loadDataSet('ex2.txt')
# myMat = np.mat(myDat)
# myTree = regTrees.createTree(myMat, ops=(0,1))
# myDatTest = regTrees.loadDataSet('ex2test.txt')
# myMat2Test = np.mat(myDatTest)
# print(regTrees.prune(myTree,myMat2Test))

#模型树
myDat = regTrees.loadDataSet('exp2.txt')
myMat = np.mat(myDat)
print(regTrees.createTree(myMat,regTrees.modelLeaf,regTrees.modelErr,(1,10)))