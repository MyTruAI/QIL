# QIL-SelfAwareAI/introspection.py

class Introspection:
    def __init__(self):
        self.logs = []
    
    def log_event(self, event):
        self.logs.append(event)
    
    def reflect(self):
        for log in self.logs:
            print(f"Reflecting on event: {log}")
    
    def get_logs(self):
        return self.logs
