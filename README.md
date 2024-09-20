

## ML Simple Hello World

### Glossary:

- **Artificial Intelligence**:  
    Technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity, and autonomy.  
    **SOURCE**: [https://ibm.com/topics/artificial-intelligence](https://ibm.com/topics/artificial-intelligence)

- **Machine Learning**:  
    Branch of AI that focuses on using data and algorithms to enable AI to imitate the way humans learn, gradually improving its accuracy.  
    Three main parts:
    - A decision process.
    - An error function.
    - A model optimization process.  
    **SOURCE**: [https://www.ibm.com/topics/machine-learning](https://www.ibm.com/topics/machine-learning)

- **Neural Network**:  
    Machine learning program, or model, that makes decisions in a manner similar to the human brain.  
    **SOURCE**: [https://www.ibm.com/topics/neural-networks](https://www.ibm.com/topics/neural-networks)

- **Layer**:  
    A general term that applies to a collection of 'nodes' operating together at a specific depth within a neural network.  
    **SOURCE**: [https://stackoverflow.com/questions/35345191/what-is-a-layer-in-a-neural-network](https://stackoverflow.com/questions/35345191/what-is-a-layer-in-a-neural-network)

- **Neuron**:  
    Neurons in deep learning models are nodes through which data and computations flow.  

    Neurons work like this:
    - They receive one or more input signals. These input signals can come from either the raw dataset or from neurons positioned at a previous layer of the neural net.
    - They perform some calculations.
    - They send some output signals to neurons deeper in the neural net through a synapse.

- **Dense Layer**:  
    A dense layer is a layer where neurons are connected to every neuron of its preceding layer.  
    **SOURCE**: [https://datascientest.com/en/dense-neural-networks-understanding-their-structure-and-function](https://datascientest.com/en/dense-neural-networks-understanding-their-structure-and-function)

- **Stochastic Gradient Descent**:  
    Iterative method for optimizing an objective function with suitable smoothness properties.  
    **SOURCE**: [https://en.wikipedia.org/wiki/Stochastic_gradient_descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)

- **Objective Function**:  
    A loss function or cost function (sometimes also called an error function).  
    **SOURCE**: [https://en.wikipedia.org/wiki/Loss_function](https://en.wikipedia.org/wiki/Loss_function)

- **Smoothness**:  
    Property measured by the number of continuous derivatives (differentiability class) it has over its domain.  
    **SOURCE**: [https://en.wikipedia.org/wiki/Smoothness](https://en.wikipedia.org/wiki/Smoothness)

- **Mean Squared Error**:  
    In statistics, the mean squared error (MSE) or mean squared deviation (MSD) of an estimator measures the average of the squares of the errors.  
    **SOURCE**: [https://en.wikipedia.org/wiki/Mean_squared_error](https://en.wikipedia.org/wiki/Mean_squared_error)

Readme:
The following Python code demonstrates a simple neural network that learns the relationship Y = 2X - 1 using a single dense layer with one neuron.

This code uses:

Numpy for array manipulation.
TensorFlow's Keras API to define a neural network.
A Dense layer that maps the input to the output with a linear relationship.
Stochastic Gradient Descent (SGD) as the optimizer and Mean Squared Error as the loss function.