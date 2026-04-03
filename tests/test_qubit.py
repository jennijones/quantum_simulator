import numpy as np
from quantum_simulator.qubit import Qubit
import pytest

def test_default_state():
    qubit = Qubit()
    assert np.allclose(qubit.state, np.array([1+0j, 0+0j], dtype=complex))

def test_one_state():
    qubit = Qubit(alpha=0+0j, beta=1+0j)
    assert np.allclose(qubit.state, np.array([0+0j, 1+0j], dtype=complex))

def test_invalid_state():
    with pytest.raises(ValueError):
        qubit = Qubit(alpha=1+0j, beta=1+0j)