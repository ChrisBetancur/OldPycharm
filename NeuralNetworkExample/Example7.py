import numpy as np
import math

softmax_output = [0.7, 0.1, 0.2]

target_output = [1, 0, 0]

loss = 0

for soft, target in zip(softmax_output, target_output):
    loss = loss + -(math.log(soft) * target)

print(loss)