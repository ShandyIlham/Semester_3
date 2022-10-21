# Program Multi Neuron Batch Input
# 1. Input layer feature 10
# 2. Per batch nya 6 input
# 3. Hidden layer 1, 5 neuron
# 4. Hidden layer 2, 3 neuron

# inisialisasi numpy
import numpy as np

# inisialisasi variabel inputs
inputs	=  [[-2, 5.5, 9, 4, 1, 6.5, -3, 7, 2.5, 6],
            [1.6, -1.7, 2.3, -0.2, 3.7, 3.3, -3.7, -3.3, 0.5, 4],
            [4.6, -2.6, 1.3, 1, -2.7, 0.5, 3.2, 4.2, -3.4, 4.7],
            [2.3, -4.1, -3.4, 1, 0.2, -4.5, 5, 1.4, 4, 36],
            [-1.3, 2, -5, 4.3, 4.5, 3.6, -0.6, -0.8, 0.5, 3.5],
            [1.2, 0.7, -4.6, -4.5, 2.2, -2.2, 3, 4.3, -1.5, 4]]

# hidden layer 1
# inisialisasi bobot hidden layer 1 
weights =  [[-3.3, 4.2, 1.8, 3.8, -4.3, -0.3, 0.9, 1.9, 2.1, 2.8],
            [4, 3.6, 4.4, -3.3, -1.8, -2.1, 1.1, 2.2, -3.9, 3.4],
            [1, -0.8, 3, 1.5, 1.2, -1.9, -2.7, 4, 0.2, 2.3],
            [2.1, -2.6, 3.9, 4.6, 0.3, -3.5, 2.2, -4.8, 4, 2.3],
            [4.1, -2.2, 0.7, 1.7, 2, 0.2, 4.6, 2.6, -2.3, 3]]

#inisialisasi bias hidden layer 1
bias = [7, 3, 0.5, 1.5, 4.5]

#output
output  = np.dot(inputs, np.array(weights).T) + bias

# hidden layer 2
# inisialisasi bobot hidden layer 2
weights2 = [[-2.1, 2.6, 2.8, -1, 3.7],
            [-1.6, 1, -0.5, 2.1, 4],
            [1.8, -4, -0.1, 1.3, 2.1]]

# inisialisasi bias hidden layer 2
bias2 = [2.5, 0.5, -4.5]

#output 2
output2 = np.dot(output, np.array(weights2).T) + bias2	

# cetak output
print(output)
print(output2)
