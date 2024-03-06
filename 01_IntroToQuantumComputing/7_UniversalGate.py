import numpy as np
import pennylane as qml


#region Codercise I.7.1
###################
# Codercise I.7.1 #
###################
# Decompose the Hadamard Gate into using only Rotation X and Rotation Z
print("======Codercise I.7.1======")
dev = qml.device("default.qubit", wires=1)

##################
# YOUR CODE HERE #
##################

# ADJUST THE VALUES OF PHI, THETA, AND OMEGA
phi, theta, omega = np.pi/2, np.pi/2, np.pi/2

@qml.qnode(dev)
def hadamard_with_rz_rx():
    qml.RZ(phi, wires=0)
    qml.RX(theta, wires=0)
    qml.RZ(omega, wires=0)
    return qml.state()

#endregion


#region Codercise I.7.2
###################
# Codercise I.7.2 #
###################
# Rewrite the given circuit over the gate set [RZ, RX]
print("======Codercise I.7.2======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def convert_to_rz_rx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE USING ONLY RZ AND RX
    # H
    qml.RZ(np.pi / 2, wires=0)
    qml.RX(np.pi / 2, wires=0)
    qml.RZ(np.pi / 2, wires=0)

    # S
    qml.RZ(np.pi / 2, wires=0)

    # T adjoint
    qml.RZ(-np.pi / 4, wires=0)

    # Y = iXZ
    qml.RX(np.pi, wires=0)
    qml.RZ(np.pi, wires=0)

    return qml.state()
#endregion


#region Codercise I.7.3
###################
# Codercise I.7.3 #
###################
# Rewrite the given circuit over the gate set [H, T]
print("======Codercise I.7.3======")
dev = qml.device("default.qubit", wires=1)


@qml.qnode(dev)
def unitary_with_h_and_t():
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY ONLY H AND T TO PRODUCE A CIRCUIT THAT EFFECTS THE GIVEN MATRIX

    qml.Hadamard(wires=0)
    qml.T(wires=0)
    qml.Hadamard(wires=0)
    qml.T(wires=0)
    qml.T(wires=0)
    qml.Hadamard(wires=0)

    return qml.state()
#endregion


