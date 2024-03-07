import numpy as np
import pennylane as qml


#region Codercise I.11.1
####################
# Codercise I.11.1 #
####################
# Write a circuit in PennyLane that accepts an integer value, then prepares
# and returns the corresponding computational basis state vector . (Assume a 3-qubit device).

print("======Codercise I.11.1======")
num_wires = 3
dev = qml.device('default.qubit', wires=num_wires)


@qml.qnode(dev)
def make_basis_state(basis_id):
    """Produce the 3-qubit basis state corresponding to |basis_id>.

    Note that the system starts in |000>.

    Args:
        basis_id (int): An integer value identifying the basis state to construct.

    Returns:
        array[complex]: The computational basis state |basis_id>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE THE BASIS STATE
    # Convert the basis id into binary with (num_wires) bits
    init_state = np.binary_repr(basis_id, width=num_wires)
    # get the index of qubits == 1
    list_of_quibits = np.where(np.array([int(x) for x in list(init_state)]) == 1)

    for i in list_of_quibits[0]:
        qml.PauliX(wires=i)

    return qml.state()
#endregion


#region Codercise I.11.2
####################
# Codercise I.11.2 #
####################
# Use PennyLane to create the state |+>|1>. Then, return two measurements:
# 1. the expectation value of  on the first qubit
# 2. the expectation value of  on the second qubit

print("======Codercise I.11.2======")
# Creates a device with *two* qubits
dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def two_qubit_circuit():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |+>|1>
    # Get the |+> on the 1st qubit
    # Get the |1> on the 2nd qubit
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)

    # RETURN TWO EXPECTATION VALUES, Y ON FIRST QUBIT, Z ON SECOND QUBIT

    return qml.expval(qml.PauliY(wires=0)), qml.expval(qml.PauliZ(wires=1))


print(two_qubit_circuit())
#endregion


#region Codercise I.11.3
####################
# Codercise I.11.3 #
####################
# Write a PennyLane circuit that creates the state . Then, measure the expectation value of the two-qubit observable
# Z x X

print("======Codercise I.11.3======")
dev = qml.device("default.qubit", wires=2)


@qml.qnode(dev)
def create_one_minus():
    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE |1>|->
    qml.PauliX(wires=0)
    qml.PauliX(wires=1)
    qml.Hadamard(wires=1)

    # RETURN A SINGLE EXPECTATION VALUE Z \otimes X

    return qml.expval(qml.PauliZ(0) @ qml.PauliX(1))


print(create_one_minus())

#endregion


#region Codercise I.11.4
####################
# Codercise I.11.4 #
####################
# Rwrite the circuits and Compare

print("======Codercise I.11.4======")
dev = qml.device('default.qubit', wires=2)


@qml.qnode(dev)
def circuit_1(theta):
    """Implement the circuit and measure Z I and I Z.

    Args:
        theta (float): a rotation angle.

    Returns:
        float, float: The expectation values of the observables Z I, and I Z
    """
    ##################
    # YOUR CODE HERE #
    ##################

    qml.RX(theta, wires=0)
    qml.RY(2 * theta, wires=1)

    return qml.expval(qml.PauliZ(0)), qml.expval(qml.PauliZ(1))


@qml.qnode(dev)
def circuit_2(theta):
    """Implement the circuit and measure Z Z.

    Args:
        theta (float): a rotation angle.

    Returns:
        float: The expectation value of the observable Z Z
    """

    ##################
    # YOUR CODE HERE #
    ##################
    qml.RX(theta, wires=0)
    qml.RY(2 * theta, wires=1)

    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))


def zi_iz_combination(ZI_results, IZ_results):
    """Implement a function that acts on the ZI and IZ results to
    produce the ZZ results. How do you think they should combine?

    Args:
        ZI_results (array[float]): Results from the expectation value of
            ZI in circuit_1.
        IZ_results (array[float]): Results from the expectation value of
            IZ in circuit_1.

    Returns:
        array[float]: A combination of ZI_results and IZ_results that
        produces results equivalent to measuring ZZ.
    """

    combined_results = np.zeros(len(ZI_results))

    ##################
    # YOUR CODE HERE #
    ##################

    return ZI_results * IZ_results


theta = np.linspace(0, 2 * np.pi, 100)

# Run circuit 1, and process the results
circuit_1_results = np.array([circuit_1(t) for t in theta])

ZI_results = circuit_1_results[:, 0]
IZ_results = circuit_1_results[:, 1]
combined_results = zi_iz_combination(ZI_results, IZ_results)

# Run circuit 2
ZZ_results = np.array([circuit_2(t) for t in theta])

# Plot your results
# plot = plotter(theta, ZI_results, IZ_results, ZZ_results, combined_results)
#endregion

