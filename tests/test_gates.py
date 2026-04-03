import numpy as np
from quantum_simulator.gates import hadamard, pauli_x, pauli_y, pauli_z

def test_hadamard_gate():
    assert(np.allclose(hadamard(), (1/np.sqrt(2)) * np.array(([1, 1], [1, -1]), dtype=complex)))

def test_pauli_x_gate():
    assert(np.allclose(pauli_x(), np.array([[0, 1], [1, 0]], dtype=complex)))

def test_pauli_y_gate():
    assert(np.allclose(pauli_y(), np.array([[0, -1j], [1j, 0]], dtype=complex)))

def test_pauli_z_gate():
    assert(np.allclose(pauli_z(), np.array([[1, 0], [0, -1]], dtype=complex)))