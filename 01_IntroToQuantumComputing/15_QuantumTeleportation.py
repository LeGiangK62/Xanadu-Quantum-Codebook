import numpy as np
import pennylane as qml


#region Codercise I.15.1
####################
# Codercise I.15.1 #
####################
#

print("======Codercise I.15.1======")


def state_preparation():
    ##################
    # YOUR CODE HERE #
    ##################

    # OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE

    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


dev = qml.device("default.qubit", wires=1)
##################
# YOUR CODE HERE #
##################


@qml.qnode(dev)
def state_prep_only():
    state_preparation()
    return qml.state()


print(state_prep_only())
#endregion


#region Codercise I.15.2
####################
# Codercise I.15.2 #
####################
#

print("======Codercise I.15.2======")


def entangle_qubits():
    ##################
    # YOUR CODE HERE #
    ##################

    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    qml.Hadamard(1)
    qml.CNOT([1, 2])
#endregion


#region Codercise I.15.3
####################
# Codercise I.15.3 #
####################
#

print("======Codercise I.15.3======")


def rotate_and_controls():
    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM THE BASIS ROTATION
    qml.CNOT([0,1])
    qml.Hadamard(0)

    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT([1,2])
    qml.CZ([0,2])
#endregion


#region Codercise I.15.4
####################
# Codercise I.15.4 #
####################
#

print("======Codercise I.15.4======")
dev = qml.device("default.qubit", wires=3)


##################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    ##################
    # YOUR CODE HERE #
    ##################

    # USE YOUR QUANTUM FUNCTIONS TO IMPLEMENT QUANTUM TELEPORTATION
    state_preparation()
    entangle_qubits()
    rotate_and_controls()
    # RETURN THE STATE

    return qml.state()


print(teleportation())

#endregion


#region Codercise I.15.5
####################
# Codercise I.15.5 #
####################
#

print("======Codercise I.15.5======")


def extract_qubit_state(input_state):
    """Extract the state of the third qubit from the combined state after teleportation.

    Args:
        input_state (array[complex]): A 3-qubit state of the form
            (1/2)(|00> + |01> + |10> + |11>) (a|0> + b|1>)
            obtained from the teleportation protocol.

    Returns:
        array[complex]: The state vector np.array([a, b]) of the third qubit.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # DETERMINE THE STATE OF THE THIRD QUBIT

    return 2 * np.array([input_state[6], input_state[7]])


# Here is the teleportation routine for you
dev = qml.device("default.qubit", wires=3)


#################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    state_preparation()
    entangle_qubits()
    rotate_and_controls()
    return qml.state()


# Print the extracted state after teleportation
full_state = teleportation()
print(extract_qubit_state(full_state))
#endregion

