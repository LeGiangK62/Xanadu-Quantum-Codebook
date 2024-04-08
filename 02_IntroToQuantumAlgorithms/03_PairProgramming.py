import pennylane as qml
import numpy as np


def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.

    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2] * len(combo))  # Index of solution
    my_array = np.identity(2 ** len(combo))  # Create the identity matrix
    my_array[index, index] = -1
    return my_array


#region Codercise A.3.1
###################
# Codercise A.3.1 #
###################
#

print("======Codercise A.3.1======")
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)


@qml.qnode(dev)
def pair_circuit(x_tilde, combo):
    """Test a pair labelled by x_tilde for the presence of a solution.

    Args:
        x_tilde (list[int]): An (n_bits - 1)-string labelling the pair to test.
        combo (list[int]): A secret combination of n_bits 0s and 1s.

    Returns:
        array[float]: Probabilities on the last qubit.
    """
    for i in range(n_bits - 1):  # Initialize x_tilde part of state
        if x_tilde[i] == 1:
            qml.PauliX(wires=i)

    ##################
    # YOUR CODE HERE #
    ##################

    qml.Hadamard(wires=n_bits - 1)
    qml.QubitUnitary(oracle_matrix(combo), wires=list(i for i in range(n_bits)))
    qml.Hadamard(wires=n_bits - 1)

    return qml.probs(wires=n_bits - 1)


#endregion

#region Codercise A.3.2
###################
# Codercise A.3.2 #
###################
#

print("======Codercise A.3.2======")


#endregion

