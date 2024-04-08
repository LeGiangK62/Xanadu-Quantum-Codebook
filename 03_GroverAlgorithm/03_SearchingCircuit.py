import pennylane as qml
import numpy as np


#region Codercise G.3.1
###################
# Codercise G.3.1 #
###################
# Define the oracle operator using the MultiControlledX gate
print("======Codercise G.3.1======")
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device('default.qubit', wires=all_wires)


def oracle(combo):
    """Implement an oracle using a multi-controlled X gate.

    Args:
        combo (list): A list of bits representing the secret combination.
    """
    combo_str = ''.join(str(j) for j in combo)
    ##################
    # YOUR CODE HERE #
    ##################
    # pass # APPLY MULTI-CONTROLLED X
    qml.MultiControlledX(control_wires=query_register, wires=aux, control_values=combo_str)
#endregion


#region Codercise G.3.2
###################
# Codercise G.3.2 #
###################
# Implement the diffusion operator in terms of the multi-controlled X

print("======Codercise G.3.2======")
def hadamard_transform(my_wires):
    """Apply the Hadamard transform on a given set of wires.

    Args:
        my_wires (list[int]): A list of wires on which the Hadamard transform will act.
    """
    for wire in my_wires:
        qml.Hadamard(wires=wire)


def diffusion():
    """Implement the diffusion operator using the Hadamard transform and
    multi-controlled X."""

    ##################
    # YOUR CODE HERE #
    ##################
    hadamard_transform(query_register)
    qml.MultiControlledX(control_wires=query_register, wires=aux, control_values="00000")

    hadamard_transform(query_register)
#endregion


#region Codercise G.3.3
###################
# Codercise G.3.3 #
###################
# Create a circuit which prepares the uniform superposition in the query register, places the auxiliary qubit in the
# state, and applies a single Grover iteration using MultiControlledX

print("======Codercise G.3.3======")


@qml.qnode(dev)
def grover_circuit(combo):
    """Apply the MultiControlledX Grover operator and return probabilities on
    query register.

    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[float]: Measurement outcome probabilities.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    # PREPARE QUERY AND AUXILIARY SYSTEM
    qml.broadcast(unitary=qml.Hadamard, wires=query_register, pattern='single')
    qml.PauliX(wires=len(combo))
    qml.Hadamard(wires=len(combo))
    # APPLY GROVER ITERATION
    oracle(combo)
    diffusion()
    return qml.probs(wires=query_register)
#endregion


