import json
from implementation.pdf_extractor import PDFExtractor
from implementation.question_answer import QuestionAnswerer
from implementation.slack_client import SlackClient
from states.extract_text_state import ExtractTextState

class PDFQuestionAnsweringAgent:
    def __init__(self, pdf_path, questions, slack_channel, slack_token, api_key,text_method):
        # define agent variable to use in each state
        self.pdf_path = pdf_path
        self.questions = questions
        self.slack_channel = slack_channel
        self.slack_token = slack_token
        self.api_key = api_key
        self.text_method = text_method
        # define the each state executor
        self.pdf_extractor = PDFExtractor
        self.question_answerer = QuestionAnswerer
        self.slack_client = SlackClient
        
        self.text = None
        self.answers = None
        # define the intial state to execute
        self.state = ExtractTextState()

    def run(self):
        while self.state:
            self.state.run(self)
