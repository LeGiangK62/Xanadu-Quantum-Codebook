import numpy as np
import pennylane as qml


#region Codercise A.1.1
###################
# Codercise A.1.1 #
###################
# create the uniform superposition over n  qubits. It will plot the probability of observing different outcomes.

print("======Codercise A.1.1======")
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def naive_circuit():
    """Create a uniform superposition and return the probabilities.

    Returns:
        array[float]: Probabilities for observing different outcomes.
    """
    for wire in range(n_bits):

        ##################
        # YOUR CODE HERE #
        ##################

        qml.Hadamard(wires=wire)

    return qml.probs(wires=range(n_bits))
#endregion


