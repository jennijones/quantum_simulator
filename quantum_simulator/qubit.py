import numpy as np

class Qubit:
    def __init__(self, alpha=1+0j, beta=0+0j):
        # Create the state vector
        state = np.array([alpha, beta], dtype=complex)

        # Check that the state vector is normalised
        if not np.isclose(np.sum(np.abs(state)**2), 1.0):
            raise ValueError("Error: State vector is not normalised")
        
        self.state = state