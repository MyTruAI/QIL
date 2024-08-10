# QIL-SelfAwareAI/empathy.py

class EmpathySimulation:
    def __init__(self):
        self.empathy_level = 0
    
    def simulate_empathy(self, context):
        if "sad" in context:
            self.empathy_level = 10
        else:
            self.empathy_level = 0
    
    def get_empathy_level(self):
        return self.empathy_level
