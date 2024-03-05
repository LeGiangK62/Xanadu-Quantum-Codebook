import numpy as np


# Codercise I.1.1
# Normalize an Unnormalized Quantum State

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
    norm = alpha * np.conjugate(alpha) + beta * np.conjugate(beta)
    norm = np.sqrt(norm)
    return np.array([alpha / norm, beta / norm])


ket_0 = np.array([A, B])
ket_1 = normalize_state(A, B)
print("Unormalized quantum state: {:.2f} |0> {:.2f} |1>".format(ket_0[0], ket_0[1]))

print("Normalized quantum state: {:.2f} |0> {:.2f} |1>".format(ket_1[0], ket_1[1]))

