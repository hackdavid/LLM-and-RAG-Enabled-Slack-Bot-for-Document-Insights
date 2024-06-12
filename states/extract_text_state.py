from .base_state import State
from .question_answer_state import AnswerQuestionsState

class ExtractTextState(State):
    def run(self, agent):
        text = agent.pdf_extractor.process(agent.pdf_path)
        if text:
            agent.text = text
            self.transition_to(agent, AnswerQuestionsState())
        else:
            print("Failed to extract text from PDF.")
            self.transition_to(agent, None)

    def transition_to(self, agent, state):
        agent.state = state
        if agent.state:
            agent.state.run(agent)

