from .base_state import State
import json
from .post_to_slack_state import PostToSlackState

class AnswerQuestionsState(State):
    def run(self, agent):
        answers = agent.question_answerer.process(agent.api_key,agent.text_method,agent.text,agent.questions)
        agent.answers = json.dumps(answers, indent=2)
        self.transition_to(agent, PostToSlackState())

    def transition_to(self, agent, state):
        agent.state = state
        if agent.state:
            agent.state.run(agent)
