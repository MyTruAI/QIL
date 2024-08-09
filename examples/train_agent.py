from qil import QuantumReinforceAgent, SimulationEnvironment

# Initialize the environment and agent
env = SimulationEnvironment()
agent = QuantumReinforceAgent()

# Start training
def start_training(agent, env):
    for episode in range(100):
        state = env.reset()
        for step in range(200):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            if done:
                break

start_training(agent, env)
