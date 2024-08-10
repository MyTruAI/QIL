# QIL-SelfAwareAI/decision_making.py

class AutonomousDecisionMaking:
    def __init__(self):
        self.goals = ["learn", "assist"]
    
    def make_decision(self, context):
        if "help" in context:
            return "assist"
        elif "new data" in context:
            return "learn"
        return "idle"
    
    def add_goal(self, goal):
        self.goals.append(goal)
    
    def get_goals(self):
        return self.goals
