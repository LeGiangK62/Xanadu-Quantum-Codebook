import numpy as np
import pennylane as qml


#region Codercise I.3.1
###################
# Codercise I.3.1 #
###################
# Create a circuit that applies U to the qubit and returns its state.

print("======Codercise I.3.1======")
dev = qml.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def apply_u():

    ##################
    # YOUR CODE HERE #
    ##################
    # USE QubitUnitary TO APPLY U TO THE QUBIT
    qml.QubitUnitary(U, wires=0)
    # Return the state
    return qml.state()
#endregion


#region Codercise I.3.2
###################
# Codercise I.3.2 #
###################
# Apply the Rot operation to a qubit using the input parameters.
print("======Codercise I.3.2======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def apply_u_as_rot(phi, theta, omega):
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY A ROT GATE USING THE PROVIDED INPUT PARAMETERS
    qml.Rot(phi, theta, omega, wires=0)
    # RETURN THE QUANTUM STATE VECTOR

    return qml.state()

#endregion

