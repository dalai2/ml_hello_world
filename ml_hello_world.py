import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential

# Simple neural network: One layer with one neuron

l0 = Dense(units=1, input_shape=[1])
# Use Sequential to define layers: one line, one layer
model = Sequential([l0])
model.compile(optimizer='sgd', loss='mean_squared_error')

# Y = 2X-1
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict(np.array([10.0])))