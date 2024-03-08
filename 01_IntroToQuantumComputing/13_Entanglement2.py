import numpy as np
import pennylane as qml


## Custom functions
def prepare_states(phi, theta, omega):
    # Just a custom function - might not behave exactly as Xanadu prepare_states function
    qml.RZ(phi, wires=0)
    qml.RY(theta, wires=0)
    qml.RZ(omega, wires=0)
    # Apply Hadamard gate to the second qubit
    qml.Hadamard(wires=1)

    # Entangle the two qubits using a CNOT gate
    qml.CNOT(wires=[0, 1])
##


#region Codercise I.13.1
####################
# Codercise I.13.1 #
####################
# Create CZ using CNOT and H

print("======Codercise I.13.1======")
dev = qml.device("default.qubit", wires=2)

# Prepare a two-qubit state; change up the angles if you like
phi, theta, omega = 1.2, 2.3, 3.4



@qml.qnode(device=dev)
def true_cz(phi, theta, omega):
    prepare_states(phi, theta, omega)

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE REGULAR CZ GATE HERE
    qml.CZ([0, 1])

    return qml.state()


@qml.qnode(dev)
def imposter_cz(phi, theta, omega):
    prepare_states(phi, theta, omega)

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT CZ USING ONLY H AND CNOT
    qml.Hadamard(1)
    qml.CNOT([0, 1])
    qml.Hadamard(1)

    return qml.state()

print(f"True CZ output state {true_cz(phi, theta, omega)}")
print(f"Imposter CZ output state {imposter_cz(phi, theta, omega)}")

#endregion


#region Codercise I.13.2
####################
# Codercise I.13.2 #
####################
# Implemente the SWAP using only CNOTs

print("======Codercise I.13.2======")
dev = qml.device("default.qubit", wires=2)

# Prepare a two-qubit state; change up the angles if you like
phi, theta, omega = 1.2, 2.3, 3.4


@qml.qnode(dev)
def apply_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE REGULAR SWAP GATE HERE
    qml.SWAP([0, 1])

    return qml.state()


@qml.qnode(dev)
def apply_swap_with_cnots(phi, theta, omega):
    prepare_states(phi, theta, omega)

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE SWAP GATE USING A SEQUENCE OF CNOTS
    qml.CNOT([0, 1])
    qml.CNOT([1, 0])
    qml.CNOT([0, 1])

    return qml.state()


print(f"Regular SWAP state = {apply_swap(phi, theta, omega)}")
print(f"CNOT SWAP state = {apply_swap_with_cnots(phi, theta, omega)}")

#endregion


#region Codercise I.13.3
####################
# Codercise I.13.3 #
####################
# Write the Controlled SWAP operation using only the Toffoli

print("======Codercise I.13.3======")
dev = qml.device("default.qubit", wires=3)

# Prepare first qubit in |1>, and arbitrary states on the second two qubits
phi, theta, omega = 1.2, 2.3, 3.4


# A helper function just so you can visualize the initial state
# before the controlled SWAP occurs.
@qml.qnode(dev)
def no_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)
    return qml.state()


@qml.qnode(dev)
def controlled_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)

    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM A CONTROLLED SWAP USING A SEQUENCE OF TOFFOLIS
    qml.Toffoli([0, 1, 2])
    qml.Toffoli([0, 2, 1])
    qml.Toffoli([0, 1, 2])

    return qml.state()


print(no_swap(phi, theta, omega))
print(controlled_swap(phi, theta, omega))

#endregion


#region Codercise I.13.4
####################
# Codercise I.13.4 #
####################
# Write a 4-qubit PennyLane circuit that applies a Hadamard to the control qubits,
# then applies a MultiControlledX on the fourth qubit, controlled on the first 3 qubits being in the state 001

print("======Codercise I.13.4======")
dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def four_qubit_mcx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT ABOVE USING A 4-QUBIT MULTI-CONTROLLED X
    qml.Hadamard(0)
    qml.Hadamard(1)
    qml.Hadamard(2)
    qml.MultiControlledX(control_wires=[0,1,2], wires=3, control_values="001")

    return qml.state()


print(four_qubit_mcx())

#endregion


#region Codercise I.13.5
####################
# Codercise I.13.5 #
####################
# Write  the 3-controlled-NOT circuit using only the Toffolis.

print("======Codercise I.13.5======")
# Wires 0, 1, 2 are the control qubits
# Wire 3 is the auxiliary qubit
# Wire 4 is the target
dev = qml.device('default.qubit', wires=5)


@qml.qnode(dev)
def four_qubit_mcx_only_tofs():
    # We will initialize the control qubits in state |1> so you can see
    # how the output state gets changed.
    qml.PauliX(wires=0)
    qml.PauliX(wires=1)
    qml.PauliX(wires=2)

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT A 3-CONTROLLED NOT WITH TOFFOLIS
    qml.Toffoli(wires=[0,1,3])
    qml.Toffoli(wires=[2,3,4])
    qml.Toffoli(wires=[0,1,3])
    return qml.state()


print(four_qubit_mcx_only_tofs())

#endregion


#region Codercise I.13.6
####################
# Codercise I.13.6 #
####################
#

print("======Codercise I.13.6======")
#endregion

