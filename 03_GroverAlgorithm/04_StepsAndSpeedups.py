import pennylane as qml
import numpy as np


#region Codercise G.4.1
###################
# Codercise G.4.1 #
###################
#
print("======Codercise G.4.1======")


def grover_iter(combo, num_steps):
    """Run Grover search for a given secret combination and a number of iterations.

    Args:
        combo (list[int]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns:
        array[float]: Probability for observing different outcomes.
    """
    n_bits = len(combo)
    query_register = list(range(n_bits))
    aux = [n_bits]
    all_wires = query_register + aux
    dev = qml.device('default.qubit', wires=all_wires)

    @qml.qnode(dev)
    def inner_circuit():
        ##################
        # YOUR CODE HERE #
        ##################
        # Init the state
        qml.broadcast(unitary=qml.Hadamard, wires=query_register, pattern='single')
        qml.PauliX(wires=len(combo))
        qml.Hadamard(wires=len(combo))

        # IMPLEMENT THE GROVER CIRCUIT
        for i in range(num_steps):
            oracle(combo)
            diffusion(n_bits)
        return qml.probs(wires=query_register)

    return inner_circuit()
#endregion


#region Codercise G.4.2
###################
# Codercise G.4.2 #
###################
#
print("======Codercise G.4.2======")
n_list = range(3,7)
opt_steps = []

for n_bits in n_list:
    combo = "0"*n_bits # A simple combination
    step_list = range(1,10) # Try out some large number of steps
    ##################
    # YOUR CODE HERE #
    ##################
    prob_iter = []
    for steps in step_list:
        probs = grover_iter(combo, int(steps))
        prob_iter.append(probs[0])
    opt_steps.append(local_max_arg(prob_iter))

print("The optimal number of Grover steps for qubits in", [3,4,5,6], "is", opt_steps, ".")

#endregion


#region Codercise G.4.3
###################
# Codercise G.4.3 #
###################
#
print("======Codercise G.4.3======")
#endregion

