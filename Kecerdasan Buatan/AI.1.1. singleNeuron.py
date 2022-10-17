# Program Single Neuron

# inisialisasi numpy
import numpy as np

# inisialisasi variable
inputs 	= [2, 5.5, 9, 4, 1, 6.5, 3, 7, 2.5, 6]

# inisialisasi bobot variable
weights	= [-3.3, 4.2, 1.8, 3.8, -4.3, -0.3, 0.9, 1.9, 2.1, 2.8]

# inisialisasi bias
bias = 7

# penghitungan  output = (input*weight)+bias
output = np.dot(weights, inputs) + bias

# cetak output
print(output)