#Import Packages
import numpy as np
import pennylane as qml


#region Codercise I.2.1
###################
# Codercise I.2.1 #
###################
# Simulate a Quantum Circuit with multiple Gates
print("======Codercise I.2.1======")


def my_circuit(theta, phi):
    ##################
    # YOUR CODE HERE #
    ##################

    # REORDER THESE 5 GATES TO MATCH THE CIRCUIT IN THE PICTURE
    qml.RX(theta, wires=2)
    qml.CNOT(wires=[0, 1])
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[2, 0])
    qml.RY(phi, wires=1)

    # This is the measurement; we return the probabilities of all possible output states
    # You'll learn more about what types of measurements are available in a later node
    return qml.probs(wires=[0, 1, 2])
#endregion


#region Codercise I.2.2
###################
# Codercise I.2.2 #
###################
# Construct a QNode, and run the circuit on the provided device.
print("======Codercise I.2.2======")
dev = qml.device("default.qubit", wires=3)


def my_circuit(theta, phi, omega):
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT BY ADDING THE GATES

    # Here are two examples, so you can see the format:
    # qml.CNOT(wires=[0, 1])
    # qml.RX(theta, wires=0)

    qml.RX(theta, wires=0)
    qml.RY(phi, wires=1)
    qml.RZ(omega, wires=2)

    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])

    return qml.probs(wires=[0, 1, 2])


# This creates a QNode, binding the function and device
my_qnode = qml.QNode(my_circuit, dev)

# We set up some values for the input parameters
theta, phi, omega = 0.1, 0.2, 0.3

# Now we can execute the QNode by calling it like we would a regular function
my_qnode(theta, phi, omega)
#endregion


#region Codercise I.2.3
###################
# Codercise I.2.3 #
###################
# Construct a QNode using decorator
print("======Codercise I.2.3======")
dev = qml.device("default.qubit", wires=3)

##################
# YOUR CODE HERE #
##################

# DECORATE THE FUNCTION BELOW TO TURN IT INTO A QNODE
@qml.qnode(dev)
def my_circuit(theta, phi, omega):
    qml.RX(theta, wires=0)
    qml.RY(phi, wires=1)
    qml.RZ(omega, wires=2)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])
    return qml.probs(wires=[0, 1, 2])


theta, phi, omega = 0.1, 0.2, 0.3

##################
# YOUR CODE HERE #
##################

# RUN THE QNODE WITH THE PROVIDED PARAMETERS
my_circuit(theta, phi, omega)

#endregion


#region Codercise I.2.4
###################
# Codercise I.2.4 #
###################
# Construct a QNode using decorator
print("======Codercise I.2.4======")
dev = qml.device("default.qubit", wires=3)

##################
# YOUR CODE HERE #
##################

# Get the circuir Depth of the Quantum Circuit
dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def my_circuit(theta, phi, omega):
    qml.RX(theta, wires=0)
    qml.RY(phi, wires=1)
    qml.RZ(omega, wires=2)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])
    return qml.probs(wires=[0, 1, 2])


##################
# YOUR CODE HERE #
##################

# FILL IN THE CORRECT CIRCUIT DEPTH
depth = 4
# Make sure of the result by the following code = Check the printed output
resource_calculator = qml.specs(my_circuit)

# we pass it the same parameters as the original QNode
theta, phi, omega = 0.1, 0.2, 0.3
print(resource_calculator(theta, phi, omega))

#endregion
