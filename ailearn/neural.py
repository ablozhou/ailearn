#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 神经网络算法
# 参考 游戏编程中的人工智能
import random

class Neuron:
'''
神经细胞
'''
    # 神经细胞输入个数
    nInputs=10
    weights=[]
    def __init__(self):
        self.nInputs=10
        self.__init__(self.nInputs)

    def __init__(self,nInputs):
        # 偏移值bias也要算一个权重, 所以权重数比input数多1
        self.nInputs=nInputs+1
        for i in xrange(self.nInputs):
            #weight random between -1,1
            weights.append(random.uniform(-1, 1))


class NeuronLayer:
'''
    神经网络的层
    '''
    #本层神经细胞数目
    nNeurons=10
    # 本层神经细胞
    neurons=[]
    def __init__(self,nNeurons,nInputsPerNeuron):
        self.nNeurons=nNeurons
        #inputs = random.randomint(10)
        for i in xrange(self.nNeurons):
            neurons.append(Neuron(nInputsPerNeuron))


class NeuralNet:
    nInput=10 #输入层节点数
    nOutput=10 # 输出个数,代表分类数
    nHidenLayer=1 #隐藏层数
    nNeuronsPerHidLyr=10 #每层的神经元数,包含一个bias
    neuronLayers=[]
    weights=[]
    bias = -1
    activeResponse = 1 
    def createNet(self):

        # 创建隐藏层
        if self.nHidenLayer > 0:
            # 创建第一个隐藏层, 其输入即初始输入
            self.neuronLayers.append(self.NeuronLayer(self.nNeuronsPerHidLyr,self.nInput))

            # 创建每个隐藏层,不包括第一个隐藏层
            for i in xrange(self.nHidenLayer-1):
                self.neuronLayers.append(self.NeuronLayer(self.nNeuronsPerHidLyr,self.nNeuronsPerHidLyr))

            # 创建输出层
            self.neuronLayers.append(self.NeuronLayer(self.nOutput,self.nNeuronsPerHidLyr))

        else:

            # 无隐藏层, 只创建输出层
            self.neuronLayers.append(self.NeuronLayer(self.nOutput,self.nInput))

    # S 逻辑函数
    def sigmoid(self,activation,response):
       return 1/(1+exp(-activation/response)) 

    # 更新函数，迭代计算每层神经网络
    def update(self,inputs[]):
        # 保存每一层的输出
        outputs=[]

        # 输入数目错误,返回空向量
        if len(inputs) != self.nInput:
            print('error, inputs number is not equals to nInput')
            return outputs
        # 对每层进行处理
        for i in xrange(self.nHidenLayer+1):
            # 多于一层隐藏层
            if i > 0:
                # 复制outputs
                inputs = outputs[:]

            outputs=[]
            # 对每个神经细胞，计算权重*input的和，并将总和抛给S形状逻辑函数
            neuronLyr = self.neuronLayers[i]
            for j in xrange(neuronLyr.nNerons):
                activation=0.0 # 神经元输出值总和初始化
                neuron = neuronLyr[j]
                for k in xrang(len(inputs)-1):
                    # 计算权重和输入值的乘积之和
                    activation += neuron.weights[k]*inputs[k]

                activation += neuron.weights[len(inputs)-1]*self.bias

                outputs[j]=sigmoid(activation,self.activeResponse)
                
        return outputs
