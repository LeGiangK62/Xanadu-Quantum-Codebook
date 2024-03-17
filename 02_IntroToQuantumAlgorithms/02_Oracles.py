import numpy as np
import pennylane as qml


#region Codercise A.2.1
###################
# Codercise A.2.1 #
###################
#  Write a function which returns the oracle in matrix form for a given secret combination.

print("======Codercise A.2.1======")


def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.

    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2] * len(combo))  # Index of solution
    my_array = np.identity(2 ** len(combo))  # Create the identity matrix

    ##################
    # YOUR CODE HERE #
    ##################

    # MODIFY DIAGONAL ENTRY CORRESPONDING TO SOLUTION INDEX
    my_array[index, index] = my_array[index, index] - 2

    return my_array
#endregion

#region Codercise A.2.1
###################
# Codercise A.2.1 #
###################
# Write a circuit which applies the oracle to the uniform superposition.

print("======Codercise A.2.1======")
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)


@qml.qnode(dev)
def oracle_circuit(combo):
    """Create a uniform superposition, apply the oracle, and return probabilities.

    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        list[float]: The output probabilities.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    for wire in range(n_bits):
        qml.Hadamard(wires=wire)
    qml.QubitUnitary(oracle_matrix(combo), wires=list(range(n_bits)))

    return qml.probs(wires=range(n_bits))

#endregion


