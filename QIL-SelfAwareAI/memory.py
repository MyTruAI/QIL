# QIL-SelfAwareAI/memory.py

class Memory:
    def __init__(self):
        self.knowledge_base = {}
    
    def learn(self, data):
        for key, value in data.items():
            self.knowledge_base[key] = value
    
    def recall(self, key):
        return self.knowledge_base.get(key, "Unknown")
    
    def update_memory(self, data):
        self.learn(data)
