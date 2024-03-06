import numpy as np
import pennylane as qml


#region Codercise I.9.1
###################
# Codercise I.9.1 #
###################
# Write a simple circuit that applies a Hadamard gate
# and returns the measurement outcome probabilities

print("======Codercise I.9.1======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def apply_h_and_measure(state):
    """Complete the function such that we apply the Hadamard gate
    and measure in the computational basis.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise leave it in state 0.

    Returns:
        array[float]: The measurement outcome probabilities.
    """
    if state == 1:
        qml.PauliX(wires=0)

    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY HADAMARD AND MEASURE
    qml.Hadamard(wires=0)

    return qml.probs(wires=0)


print(apply_h_and_measure(0))
print(apply_h_and_measure(1))
#endregion


#region Codercise I.9.2a
####################
# Codercise I.9.2a #
####################

print("======Codercise I.9.2a======")
# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>
def prepare_psi():
    qml.RX(-2 * np.pi / 3, wires=0)


# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    qml.Hadamard(wires=0)
    qml.S(wires=0)
#endregion


#region Codercise I.9.2b
###################
# Codercise I.9.2b #
###################
#

print("======Codercise I.9.2b======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def measure_in_y_basis():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE THE STATE
    prepare_psi()
    # PERFORM THE ROTATION BACK TO COMPUTATIONAL BASIS
    qml.adjoint(y_basis_rotation)()
    # RETURN THE MEASUREMENT OUTCOME PROBABILITIES

    return qml.probs(wires=0)


print(measure_in_y_basis())

#endregion





