from qiskit import QuantumCircuit, transpile, execute
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

def compile_and_execute_qil(qil_code):
    try:
        qc = create_complex_quantum_circuit(qil_code)
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc, backend, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        plot_histogram(counts).show()
        return counts
    except Exception as e:
        print(f"Error during QIL execution: {e}")
        return None

def create_complex_quantum_circuit(encoded_action):
    qc = QuantumCircuit(3, 3)
    for i, bit in enumerate(encoded_action):
        if bit == '1':
            qc.x(i)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cz(0, 2)
    qc.ry(np.pi / 4, 0)
    qc.ry(np.pi / 4, 1)
    qc.ry(np.pi / 4, 2)
    qc.barrier()
    qc.crz(np.pi / 2, 0, 1)
    qc.crz(np.pi / 2, 1, 2)
    qc.crz(np.pi / 2, 0, 2)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc
