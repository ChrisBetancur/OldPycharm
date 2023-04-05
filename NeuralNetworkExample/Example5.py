import math
import numpy as np

layer_outputs = [4.8, 1.21, 2.385]

# layer_outputs = [4.8, 4.79, 4.25]

E = math.e

exp_values = []

for output in layer_outputs:
    exp_values.append(E**output)

#print(exp_values)

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)

# print(norm_values)
# print(sum(norm_values))

layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]

exp_values = np.exp(layer_outputs)
norm_values = exp_values / np.sum(exp_values, axis=1,keepdims=True)

print(norm_values)
# print(sum(norm_values))