import pennylane as qml
import numpy as np


#region Codercise G.5.1
###################
# Codercise G.5.1 #
###################
# Create an oracle for a random solution set of a given size using the MultiControlledX gate.
print("======Codercise G.5.1======")
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device('default.qubit', wires=all_wires)


def oracle_multi(combos):
    """Implement multi-solution oracle using sequence of multi-controlled X gates.

    Args:
        combos (list[list[int]]): A list of solutions.
    """
    for combo in combos:
        combo_str = ''.join(str(j) for j in combo)
        ##################
        # YOUR CODE HERE #
        ##################
        qml.MultiControlledX(control_wires=query_register, wires=aux, control_values=combo_str)


#endregion


#region Codercise G.5.2a
###################
# Codercise G.5.2a #
###################
# Using the oracle from the previous exercise, construct the circuit for multi-solution Grover search!
print("======Codercise G.5.2a======")
n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qml.device('default.qubit', wires=all_wires, shots=None)


def grover_iter_multi(combos, num_steps):
    """Run Grover search for multiple secret combinations and a number
    of Grover steps.

    Args:
        combos (list[list[int]]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns:
        array[float]: Probability for observing different outcomes.
    """

    @qml.qnode(dev)
    def inner_circuit():
        qml.PauliX(wires=n_bits)
        qml.Hadamard(wires=n_bits)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            ##################
            # YOUR CODE HERE #
            ##################
            oracle_multi(combos)
            diffusion(n_bits)

        return qml.probs(wires=query_register)

    return inner_circuit()


#endregion


#region Codercise G.5.2b
###################
# Codercise G.5.2b #
###################
# Determine the optimal number of steps for Grover search
print("======Codercise G.5.2b======")
m_list = range(3)
opt_steps = []

for m_bits in m_list:
    combos = [[int(s) for s in np.binary_repr(j, n_bits)] for j in range(2 ** m_bits)]
    step_list = range(1, 10)
    ##################
    # YOUR CODE HERE #
    ##################
    probs = []
    for num_steps in step_list:
        probs.append(grover_iter_multi(combos, num_steps)[0])
    opt_steps.append(local_max_arg(probs))

print("The optimal number of Grover steps for the number of solutions in", [1, 2, 4], "is", opt_steps, ".")
#endregion