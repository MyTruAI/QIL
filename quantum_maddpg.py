from qiskit import Aer
from qiskit.circuit.library import RealAmplitudes
from qiskit_machine_learning.neural_networks import TwoLayerQNN
from maddpg.maddpg import MADDPG

class QuantumMADDPG(MADDPG):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.backend = Aer.get_backend('statevector_simulator')
        self.feature_map = RealAmplites(num_qubits=2, entanglement='full')
        num_inputs = 2
        self.qnn = TwoLayerQNN(num_qubits=num_inputs, feature_map=self.feature_map, quantum_instance=self.backend)

    def act(self, state):
        qnn_output = self.qnn.forward(state)
        if qnn_output > 0.5:
            return 1
        else:
            return 0
