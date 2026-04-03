import numpy as np

def hadamard():
    """
    Returns the Hadamard gate as a 2x2 numpy array. 
    The Hadamard gate transforms a general state α|0⟩ + β|1⟩ into (α+β)/√2 |0⟩ + (α-β)/√2 |1⟩, e.g. |0> or |1> becomes an equal superposition of both states.
    """
    return (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
 
def pauli_x():
    """
    Returns the Pauli X gate as a 2x2 numpy array.
    The Pauli X gate flips the state of a qubit, e.g. |0> to |1> and |1> to |0>, akin to a classical NOT gate. 
    """
    return np.array([[0, 1], [1, 0]], dtype=complex)

def pauli_y():
    """
    Returns the Pauli Y gate as a 2x2 numpy array.
    The Pauli Y gate both flips the state of a qubit and adds a phase shift, e.g. transforming |0> to i|1> and |1> to -i|0>. 
    """
    return np.array([[0, -1j], [1j, 0]], dtype=complex)

def pauli_z():
    """
    Returns the Pauli Z gate as a 2x2 numpy array
    The Pauli Z gate flips the phase of the |1> element of a state, e.g. |0> remains unchanged but |1> becomes -|1>.
    """
    return np.array([[1, 0], [0, -1]], dtype=complex)