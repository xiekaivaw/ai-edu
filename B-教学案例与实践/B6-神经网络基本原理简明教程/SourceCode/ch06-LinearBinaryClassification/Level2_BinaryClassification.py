# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import numpy as np

from HelperClass.NeuralNet12 import *
   
# 主程序
if __name__ == '__main__':
    # data
    reader = DataReader11()
    reader.ReadData()
    # net
    num_input = 2
    num_output = 1
    params = HyperParameters11(num_input, num_output, eta=0.1, max_epoch=100, batch_size=10, eps=1e-3, net_type=NetType.BinaryClassifier)
    net = NeuralNet12(params)
    net.train(reader, checkpoint=1)

    # inference
    x_predicate = np.array([0.58,0.92,0.62,0.55,0.39,0.29]).reshape(3,2)
    a = net.inference(x_predicate)
    print("A=", a)




