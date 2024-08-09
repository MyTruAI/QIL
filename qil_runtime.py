class QILRuntime:
    def execute(self, compiled_code):
        try:
            result = compiled_code.result()
            return result
        except Exception as e:
            print(f"Error during execution: {e}")
            return None
