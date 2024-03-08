import numpy as np
import pennylane as qml


#region Codercise I.14.1
####################
# Codercise I.14.1 #
####################
# Write a set of 4 circuits that prepare and return each of the four Bell states.

print("======Codercise I.14.1======")
dev = qml.device('default.qubit', wires=2)


# Starting from the state |00>, implement a PennyLane circuit
# to construct each of the Bell basis states.

@qml.qnode(dev)
def prepare_psi_plus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE (1/sqrt(2)) (|00> + |11>)
    qml.Hadamard(0)
    qml.CNOT([0, 1])

    return qml.state()


@qml.qnode(dev)
def prepare_psi_minus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE (1/sqrt(2)) (|00> - |11>)
    # qml.PauliX(0)
    qml.Hadamard(0)
    qml.PauliZ(0)
    qml.CNOT([0, 1])

    return qml.state()


@qml.qnode(dev)
def prepare_phi_plus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE  (1/sqrt(2)) (|01> + |10>)
    qml.Hadamard(0)
    qml.PauliX(1)
    qml.CNOT([0, 1])

    return qml.state()


@qml.qnode(dev)
def prepare_phi_minus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE  (1/sqrt(2)) (|01> - |10>)
    # qml.PauliX(0)
    qml.Hadamard(0)
    qml.PauliZ(0)
    qml.PauliX(1)
    qml.CNOT([0, 1])

    return qml.state()


psi_plus = prepare_psi_plus()
psi_minus = prepare_psi_minus()
phi_plus = prepare_phi_plus()
phi_minus = prepare_phi_minus()

# Uncomment to print results
# print(f"|ψ_+> = {psi_plus}")
# print(f"|ψ_-> = {psi_minus}")
# print(f"|ϕ_+> = {phi_plus}")
# print(f"|ϕ_-> = {phi_minus}")

#endregion


#region Codercise I.14.2
####################
# Codercise I.14.2 #
####################
# Implement a 3-qubit circuit in PennyLane that can perform the following:
#
# If the first two qubits are both |0>, do nothing
# If the first qubit is |0> and the second is |1>, apply PauliX to the third qubit
# If the first qubit is |1> and the second is |0>, apply PauliZ to the third qubit
# If the first two qubits are both |1>, apply a PauliY operation the third qubit

print("======Codercise I.14.2======")
dev = qml.device("default.qubit", wires=3)

# State of first 2 qubits
state = [0, 1]


@qml.qnode(device=dev)
def apply_control_sequence(state):
    # Set up initial state of the first two qubits
    if state[0] == 1:
        qml.PauliX(wires=0)
    if state[1] == 1:
        qml.PauliX(wires=1)

        # Set up initial state of the third qubit - use |->
    # so we can see the effect on the output
    qml.PauliX(wires=2)
    qml.Hadamard(wires=2)

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE MULTIPLEXER
    # IF STATE OF FIRST TWO QUBITS IS 01, APPLY X TO THIRD QUBIT
    # Controlled - controlled - X is Toffoli
    qml.PauliX(0)
    qml.Toffoli([0, 1, 2])
    qml.PauliX(0)

    # IF STATE OF FIRST TWO QUBITS IS 10, APPLY Z TO THIRD QUBIT
    # We have Z = HXH
    qml.PauliX(1)
    qml.Hadamard(2)
    qml.Toffoli([0, 1, 2])
    qml.Hadamard(2)
    qml.PauliX(1)

    # IF STATE OF FIRST TWO QUBITS IS 11, APPLY Y TO THIRD QUBIT
    # We have Y = SXS* => Remember to reversed the process (right to left)
    qml.adjoint(qml.S)(2)
    qml.Toffoli([0, 1, 2])
    qml.S(2)

    return qml.state()

#endregion


#region Codercise I.14.3
####################
# Codercise I.14.3 #
####################
#

print("======Codercise I.14.3======")

#endregion

