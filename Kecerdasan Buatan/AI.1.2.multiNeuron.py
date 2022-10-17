# Program Multi Neuron

# inisialisasi numpy
import numpy as np

# inisialisasi variable
inputs  = [2, 5.5, 9, 4, 1, 6.5, 3, 7, 2.5, 6]

# inisialisasi bobot variable
weights =  [[-3.3, 4.2, 1.8, 3.8, -4.3, -0.3, 0.9, 1.9, 2.1, 2.8],
            [4, 3.6, 4.4, -3.3, -1.8, -2.1, 1.1, 2.2, -3.9, 3.4],
            [1, -0.8, 3, 1.5, 1.2, -1.9, -2.7, 4, 0.2, 2.3],
            [2.1, -2.6, 3.9, 4.6, 0.3, -3.5, 2.2, -4.8, 4, 2.3],
            [4.1, -2.2, 0.7, 1.7, 2, 0.2, 4.6, 2.6, -2.3, 3]]

# inisialisasi bias
bias = [7, 3, 0.5, 1.5, 4.5]

# penghitungan output = (input*weight)+bias
output = np.dot(weights, inputs) + bias

# cetak output
print(output)