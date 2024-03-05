import numpy as np

#region Codercise I.1.1
##################
# Codercise I.1.1#
##################
# Normalize an Unnormalized Quantum State
print("======Codercise I.1.1======")


A = 2.0 + 1.0j
B = -0.3 + 0.4j


def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.

        Args:
            alpha (complex): The amplitude associated with the |0> state.
            beta (complex): The amplitude associated with the |1> state.

        Returns:
            array[complex]: A vector (numpy array) with 2 elements that represents
            a normalized quantum state.
            CREATE A VECTOR [a', b'] BASED ON alpha AND beta SUCH THAT |a'|^2 + |b'|^2 = 1
        """
    norm = np.abs(alpha) ** 2 + np.abs(beta) ** 2
    norm = np.sqrt(norm)
    return np.array([alpha / norm, beta / norm])


ket_0 = np.array([A, B])
ket_1 = normalize_state(A, B)
print("Unormalized quantum state: {:.2f} |0> {:.2f} |1>".format(ket_0[0], ket_0[1]))
print("Normalized quantum state: {:.2f} |0> {:.2f} |1>".format(ket_1[0], ket_1[1]))
#endregion


#region Codercise I.1.2
##################
# Codercise I.1.2#
##################
# Compute the Inner Broduct between two arbitrary states
print("======Codercise I.1.2======")


def bra_state(state):
    return np.array([np.conj(state[0]), np.conj(state[1])])


def inner_product(state_1, state_2):
    """Compute the inner product between two states.

    Args:
        state_1 (array[complex]): A normalized quantum state vector
        state_2 (array[complex]): A second normalized quantum state vector

    Returns:
        complex: The value of the inner product <state_1 | state_2>.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    # calculate the ket of state_1
    bra_1 = bra_state(state_1)
    # COMPUTE AND RETURN THE INNER PRODUCT
    return bra_1[0] * state_2[0] + bra_1[1] * state_2[1]


# Test your results with this code
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

print(f"<0|0> = {inner_product(ket_0, ket_0)}")
print(f"<0|1> = {inner_product(ket_0, ket_1)}")
print(f"<1|0> = {inner_product(ket_1, ket_0)}")
print(f"<1|1> = {inner_product(ket_1, ket_1)}")
#endregion


#region Codercise I.1.3
###################
# Codercise I.1.3 #
###################
# Quantum Measurement - Returen list based on the probabilities given by the inpute state
print("======Codercise I.1.3======")


def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (array[complex]): A normalized qubit state vector.
        num_meas (int): The number of measurements to take

    Returns:
        array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability
        distribution defined by the input state.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # COMPUTE THE MEASUREMENT OUTCOME PROBABILITIES

    p0 = np.abs(state[0]) ** 2
    p1 = np.abs(state[1]) ** 2

    # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES

    return np.random.choice(np.array([0,1]), size=num_meas, p=[p0, p1])


st = np.array([0.8, 0.6])
print(measure_state(st, 10))


#endregion


#region Codercise I.1.4
###################
# Codercise I.1.4 #
###################
# Apply the opertion U to the quantum state
print("======Codercise I.1.4======")
U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


def apply_u(state):
    """Apply a quantum operation.

    Args:
        state (array[complex]): A normalized quantum state vector.

    Returns:
        array[complex]: The output state after applying U.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY U TO THE INPUT STATE AND RETURN THE NEW STATE
    return np.dot(U, state)

#endregion

U = np.array([[0, 1], [1, 0]])
state = np.array([0.8, 0.6])

print(apply_u(state))

#region Codercise I.1.5
##################
# Codercise I.1.5 #
##################
# Simulate a Quantum Algorithm

print("======Codercise I.1.5======")

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


def initialize_state():
    """Prepare a qubit in state |0>.

    Returns:
        array[float]: the vector representation of state |0>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE THE STATE |0>
    return np.array([1, 0])


def quantum_algorithm():
    """Use the functions above to implement the quantum algorithm described above.

    Try and do so using three lines of code or less!

    Returns:
        array[int]: the measurement results after running the algorithm 100 times
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # PREPARE THE STATE, APPLY U, THEN TAKE 100 MEASUREMENT SAMPLES
    init = initialize_state()

    applied = apply_u(init)

    return measure_state(applied, 100)


print(quantum_algorithm())
#endregion


