from .base_state import State

class PostToSlackState(State):
    def run(self, agent):
        result = agent.slack_client.process(agent.slack_token,agent.slack_channel, agent.answers)
        if result:
            print("Posted results to Slack successfully.")
        self.transition_to(agent, None)

    def transition_to(self, agent, state):
        agent.state = state
        if agent.state:
            agent.state.run(agent)
