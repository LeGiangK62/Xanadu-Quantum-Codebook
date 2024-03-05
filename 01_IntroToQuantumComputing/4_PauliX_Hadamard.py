import numpy as np
import pennylane as qml


#region Codercise I.4.1
###################
# Codercise I.4.1 #
###################
# Using qml.PauliX to initialize the qubit's state to  or  based on an input flag.
# Then, use qml.QubitUnitary to apply the provided U.
print("======Codercise I.4.1======")
dev = qml.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


@qml.qnode(dev)
def varied_initial_state(state):
    """Complete the function such that we can apply the operation U to
    either |0> or |1> depending on the input argument flag.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    # KEEP THE QUBIT IN |0> OR CHANGE IT TO |1> DEPENDING ON THE state PARAMETER

    if state:
        qml.PauliX(wires=0)
    # APPLY U TO THE STATE
    qml.QubitUnitary(U, wires=0)

    return qml.state()
#region


#region Codercise I.4.2
###################
# Codercise I.4.2 #
###################
# Apply a Hadamard gate to the qubit,
# returns the state of the qubit with qml.state.
print("======Codercise I.4.2======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def apply_hadamard():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY THE HADAMARD GATE
    qml.Hadamard(wires=0)
    # RETURN THE STATE
    return qml.state()

#endregion


#region Codercise I.4.3
###################
# Codercise I.4.3 #
###################
# Apply the Hadamard to either |0> or |1>
# depending on the input argument flag.
dev = qml.device("default.qubit", wires=1)
print("======Codercise I.4.3======")


@qml.qnode(dev)
def apply_hadamard_to_state(state):
    """Complete the function such that we can apply the Hadamard to
    either |0> or |1> depending on the input argument flag.

    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    ##################
    # YOUR CODE HERE #
    ##################

    # KEEP THE QUBIT IN |0> OR CHANGE IT TO |1> DEPENDING ON state
    if state:
        qml.PauliX(wires=0)

    # APPLY THE HADAMARD
    qml.Hadamard(wires=0)
    # RETURN THE STATE

    return qml.state()


print(apply_hadamard_to_state(0))
print(apply_hadamard_to_state(1))
#endregion


#region Codercise I.4.4
###################
# Codercise I.4.4 #
###################
# Create a circuit consisting 3 Gates H - X - H.
print("======Codercise I.4.4======")

##################
# YOUR CODE HERE #
##################

# CREATE A DEVICE
dev = qml.device("default.qubit", wires=1)


# CREATE A QNODE CALLED apply_hxh THAT APPLIES THE CIRCUIT ABOVE
@qml.qnode(dev)
def apply_hxh(state):
    if state:
        qml.PauliX(wires=0)

    qml.Hadamard(wires=0)
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)

    return qml.state()


# Print your results
print(apply_hxh(0))
print(apply_hxh(1))

#endregion
