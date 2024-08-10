# QIL-SelfAwareAI/quantum_action.py

from qiskit import QuantumCircuit, Aer, transpile, execute

def encode_action(action_text):
    binary_representation = ''.join(format(ord(char), '08b') for char in action_text)
    truncated_binary = binary_representation[:3].ljust(3, '0')
    return truncated_binary

def create_quantum_circuit(encoded_action):
    qc = QuantumCircuit(3, 3)
    for i, bit in enumerate(encoded_action):
        if bit == '1':
            qc.x(i)
    qc.h(range(3))
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cz(0, 2)
    qc.measure(range(3), range(3))
    return qc

def execute_quantum_circuit(qc):
    backend = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(qc, backend)
    job = execute(compiled_circuit, backend, shots=1024)
    result = job.result()
    counts = result.get_counts()
    return counts

def determine_classification(counts):
    max_count = max(counts, key=counts.get)
    classification_map = {
        '000': "Goodness",
        '001': "Passion",
        '010': "Ignorance",
        '011': "Thought",
        '100': "Word",
        '101': "Deed",
        '110': "Intention",
        '111': "Consequence"
    }
    return classification_map.get(max_count, "Unknown")

def map_classification_to_action(classification):
    action_mapping = {
        "Goodness": 1,
        "Passion": 0,
        "Ignorance": -1,
        "Thought": 1,
        "Word": 0,
        "Deed": -1,
        "Intention": 1,
        "Consequence": -1,
        "Unknown": 0
    }
    return action_mapping.get(classification, 0)
