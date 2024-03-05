import numpy as np
import pennylane as qml


#region Codercise I.5.1
###################
# Codercise I.5.1 #
###################
# Apply qml.PauliZ to the  state and returns the state
#
print("======Codercise I.5.1======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def apply_z_to_plus():
    """Write a circuit that applies PauliZ to the |+> state and returns
    the state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE |+> STATE
    qml.Hadamard(wires=0)

    # APPLY PAULI Z
    qml.PauliZ(wires=0)
    # RETURN THE STATE
    return qml.state()


print(apply_z_to_plus())
#endregion

#region Codercise I.5.2
###################
# Codercise I.5.2 #
###################
# Apply qml.PauliZ using the Rotation Z qml.RZ
#
print("======Codercise I.5.2======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def fake_z():
    """Use RZ to produce the same action as Pauli Z on the |+> state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE |+> STATE
    qml.Hadamard(wires=0)
    # APPLY RZ
    qml.RZ(np.pi, wires=0)
    # RETURN THE STATE
    return qml.state()
#endregion


#region Codercise I.5.3
###################
# Codercise I.5.3 #
###################
# Implement the given circuit, using adjoints when necessary,
# and return the quantum state
print("======Codercise I.5.3======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def many_rotations():
    """Implement the circuit depicted above and return the quantum state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT
    qml.Hadamard(wires=0)
    qml.S(wires=0)
    qml.adjoint(qml.T)(wires=0)
    qml.RZ(0.3, wires=0)
    qml.adjoint(qml.S)(wires=0)
    # RETURN THE STATE

    return qml.state()

#endregion


#region Codercise I.5.4
###################
# Codercise I.5.4 #
###################
# Optimize the given circuit with a lot of T gate
#
print("======Codercise I.5.4======")
dev = qml.device('default.qubit', wires=3)


@qml.qnode(dev)
def too_many_ts():
    """You can implement the original circuit here as well, it may help you with
    testing to ensure that the circuits have the same effect.

    Returns:
        array[float]: The measurement outcome probabilities.
    """
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    qml.T(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    qml.T(wires=0)

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=0)
    qml.adjoint(qml.T)(wires=1)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=0)
    qml.adjoint(qml.T)(wires=1)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)
    qml.T(wires=1)

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    return qml.probs(wires=[0, 1, 2])


@qml.qnode(dev)
def just_enough_ts():
    """Implement an equivalent circuit as the above with the minimum number of
    T and T^\dagger gates required.

    Returns:
        array[float]: The measurement outcome probabilities.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT, BUT COMBINE AND OPTIMIZE THE GATES
    # TO MINIMIZE THE NUMBER OF TS

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    qml.S(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T)(wires=2)

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    qml.adjoint(qml.S)(wires=0)
    qml.PauliZ(wires=1)
    qml.adjoint(qml.S)(wires=2)
    qml.adjoint(qml.T)(wires=2)

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    return qml.probs(wires=[0, 1, 2])


##################
# YOUR CODE HERE #
##################

# FILL IN THE CORRECT VALUES FOR THE ORIGINAL CIRCUIT
original_depth = 8
original_t_count = 13
original_t_depth = 6

# FILL IN THE CORRECT VALUES FOR THE NEW, OPTIMIZED CIRCUIT
optimal_depth = 6
optimal_t_count = 3
optimal_t_depth = 2
#endregion
