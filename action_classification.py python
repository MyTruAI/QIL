def classify_action(action_text):
    encoded_action = encode_action(action_text)
    qc = create_complex_quantum_circuit(encoded_action)
    
    transpiled_qc = transpile(qc, backend)
    qobj = assemble(transpiled_qc)
    result = execute(transpiled_qc, backend, shots=1024).result()
    counts = result.get_counts()
    
    max_count = max(counts, key=counts.get)
    if max_count == '000':
        classification = "Goodness"
    elif max_count == '001':
        classification = "Passion"
    elif max_count == '010':
        classification = "Ignorance"
    else:
        classification = "Unknown"
    
    return classification

def encode_action(action_text):
    binary_representation = ''.join(format(ord(char), '08b') for char in action_text)
    truncated_binary = binary_representation[:2].ljust(2, '0')
    return truncated_binary
