# components/slack_client.py
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    
    @classmethod
    def process(cls,token, channel, text):
        client = WebClient(token=token)
        try:
            response = client.chat_postMessage(
                channel=channel,
                text=text
            )
            return response
        except SlackApiError as e:
            print(f"Error posting to Slack: {e}")
            return None
