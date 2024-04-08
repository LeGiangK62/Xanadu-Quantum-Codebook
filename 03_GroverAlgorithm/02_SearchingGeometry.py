import pennylane as qml
import numpy as np


#region Codercise G.2.1
###################
# Codercise G.2.1 #
###################
# Determine the optimal number of Grover steps for 5 bits

print("======Codercise G.2.1======")
n_bits = 5
dev = qml.device("default.qubit", wires=n_bits)

def oracle_matrix(combo):
    """Return the oracle matrix for a secret combination.

    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        array[float]: The matrix representation of the oracle.
    """
    index = np.ravel_multi_index(combo, [2 ] *len(combo)) # Index of solution
    my_array = np.identity( 2**len(combo)) # Create the identity matrix
    my_array[index, index] = -1
    return my_array

def diffusion_matrix():
    """Return the diffusion matrix.

    Returns:
        array[float]: The matrix representation of the diffusion operator.
    """
    psi_piece = ( 1 / 2**n_bits ) *np.ones( 2**n_bits)
    ident_piece = np.eye( 2**n_bits)
    return ( 2 *psi_piece - ident_piece)

@qml.qnode(dev)
def grover_circuit(combo, num_steps):
    """Apply the Grover operator num_steps times to the uniform superposition
       and return the state.

    Args:
        combo (list[int]): A list of bits representing the secret combination.
        num_steps (int): The number of iterations of the Grover operator
            our circuit is to perform.

    Returns:
        array[complex]: The quantum state (amplitudes) after repeated Grover
        iterations.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    qml.broadcast(unitary=qml.Hadamard, wires=list(range(n_bits)), pattern='single')
    for i in range(num_steps):
        qml.QubitUnitary(oracle_matrix(combo), wires=list(range(n_bits)))
        qml.QubitUnitary(diffusion_matrix(), wires=list(range(n_bits)))

    return qml.state()

my_steps = 4 # YOUR STEP NUMBER HERE
#endregion

