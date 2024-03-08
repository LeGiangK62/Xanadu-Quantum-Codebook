import numpy as np
import pennylane as qml


#region Codercise I.12.1
####################
# Codercise I.12.1 #
####################
# Write a circuit that implements a CNOT gate between two qubits. Test it out on all four computational basis states.
# What are the resulting states?

print("======Codercise I.12.1======")

num_wires = 2
dev = qml.device('default.qubit', wires=num_wires)


@qml.qnode(dev)
def apply_cnot(basis_id):
    """Apply a CNOT to |basis_id>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        array[complex]: The resulting state after applying CNOT|basis_id>.
    """

    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=len(dev.wires))]
    qml.BasisStatePreparation(bits, wires=[0, 1])

    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY THE CNOT
    qml.CNOT(wires=[0, 1])
    return qml.state()


##################
# YOUR CODE HERE #
##################

# REPLACE THE BIT STRINGS VALUES BELOW WITH THE CORRECT ONES
cnot_truth_table = {
    "00": "00",
    "01": "01",
    "10": "11",
    "11": "10"
}

# Run your QNode with various inputs to help fill in your truth table
print(apply_cnot(3))

#endregion


#region Codercise I.12.2
####################
# Codercise I.12.2 #
####################
# Implement the given circuit and inspect the output state. Is this state separable or entangled?

print("======Codercise I.12.2======")
dev = qml.device("default.qubit", wires=2)


@qml.qnode(dev)
def apply_h_cnot():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY THE OPERATIONS IN THE CIRCUIT
    qml.Hadamard(0)
    qml.CNOT(wires=[0,1])

    return qml.state()


print(apply_h_cnot())

##################
# YOUR CODE HERE #
##################

# SET THIS AS 'separable' OR 'entangled' BASED ON YOUR OUTCOME
state_status = "entangled"
#endregion


#region Codercise I.12.3
####################
# Codercise I.12.3 #
####################
# Write a circuit in PennyLane that implements the given sequence of operations.
# Return the measurement outcome probabilities.

print("======Codercise I.12.3======")
dev = qml.device('default.qubit', wires=3)


@qml.qnode(dev)
def controlled_rotations(theta, phi, omega):
    """Implement the circuit above and return measurement outcome probabilities.

    Args:
        theta (float): A rotation angle
        phi (float): A rotation angle
        omega (float): A rotation angle

    Returns:
        array[float]: Measurement outcome probabilities of the 3-qubit
        computational basis states.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY THE OPERATIONS IN THE CIRCUIT AND RETURN MEASUREMENT PROBABILITIES
    qml.Hadamard(0)
    qml.CRX(theta, wires=[0, 1])
    qml.CRY(phi, wires=[1, 2])
    qml.CRZ(omega, wires=[2, 0])

    return qml.probs(wires=[0, 1, 2])


theta, phi, omega = 0.1, 0.2, 0.3
print(controlled_rotations(theta, phi, omega))
#endregion


