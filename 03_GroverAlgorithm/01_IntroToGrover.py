import pennylane as qml
import numpy as np

#region Codercise G.1.1
###################
# Codercise G.1.1 #
###################
#Returning the amplitudes after applying the oracle to the uniform superposition.

print("======Codercise G.1.1======")
n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)


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


@qml.qnode(dev)
def oracle_amp(combo):
    """Prepare the uniform superposition and apply the oracle.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    qml.broadcast(unitary=qml.Hadamard, wires=list(range(n_bits)), pattern='single')
    qml.QubitUnitary(oracle_matrix(combo), wires=list(range(n_bits)))

    return qml.state()
#endregion


#region Codercise G.1.2
###################
# Codercise G.1.2 #
###################
# Define the diffusion operator as a matrix, and visualize its effect on the amplitudes in the post-oracle state

print("======Codercise G.1.2======")
n_bits = 4


def diffusion_matrix():
    """Return the diffusion matrix.

    Returns:
        array[float]: The matrix representation of the diffusion operator.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return 1/(2 ** (n_bits-1)) * np.ones(2 ** n_bits) - np.eye(2 ** n_bits)
    # pass # FORM A DIFFERENCE OF MATRICES


@qml.qnode(dev)
def difforacle_amp(combo):
    """Apply the oracle and diffusion matrix to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The quantum state (amplitudes) after applying the oracle
        and diffusion.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    qml.broadcast(unitary=qml.Hadamard, wires=list(range(n_bits)), pattern='single')
    qml.QubitUnitary(oracle_matrix(combo), wires=list(range(n_bits)))
    qml.QubitUnitary(diffusion_matrix(), wires=list(range(n_bits)))
    return qml.state()

#endregion


#region Codercise G.1.3
###################
# Codercise G.1.3 #
###################
# Amplify the amplitude for the solution state using two Grover iterations

print("======Codercise G.1.3======")


@qml.qnode(dev)
def two_difforacle_amp(combo):
    """Apply the Grover operator twice to the uniform superposition.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[complex]: The resulting quantum state.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    qml.broadcast(unitary=qml.Hadamard, wires=list(range(n_bits)), pattern='single')
    qml.QubitUnitary(oracle_matrix(combo), wires=list(range(n_bits)))
    qml.QubitUnitary(diffusion_matrix(), wires=list(range(n_bits)))
    qml.QubitUnitary(oracle_matrix(combo), wires=list(range(n_bits)))
    qml.QubitUnitary(diffusion_matrix(), wires=list(range(n_bits)))
    return qml.state()
#endregion

