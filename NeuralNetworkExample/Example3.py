import numpy as np
from nnfs.datasets import spiral_data
import nnfs

# For tutorial to get same results as video, book
nnfs.init()

# Batch

X, y = spiral_data(100, 3)


class LayerDense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        self.output = None

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class ActivationReLU:
    def foward(self, inputs):
        self.output = np.maximum(0, inputs)


class ActivationSoftmax:
    def foward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities


'''layer1 = LayerDense(2, 5)
activation1 = ActivationReLU()

layer1.forward(X)
print(layer1.output)
print()
activation1.foward(layer1.output)
print(activation1.output)'''

'''layer2 = LayerDense(5, 2)

layer1.forward(X)
print(layer1.output)
print()
layer2.forward(layer1.output)
print(layer2.output)'''

dense1 = LayerDense(2, 3)
activation1 = ActivationReLU()

dense2 = LayerDense(3, 3)
activation2 = ActivationSoftmax()

dense1.forward(X)
activation1.foward(dense1.output)

dense2.forward(activation1.output)
activation2.foward(dense2.output)

print(activation2.output[:5])


