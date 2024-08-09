from qil import compile_and_execute_qil

# Example QIL code
qil_code = "create_complex_quantum_circuit('010')"
result = compile_and_execute_qil(qil_code)
print("Result:", result)
