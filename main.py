# main.py
import yaml
import argparse
from agent import PDFQuestionAnsweringAgent

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main(config_path):
    config = load_config(config_path)
    pdf_path = config["pdf_path"]
    questions = config["questions"]
    slack_channel = config["slack_channel"]
    slack_token = config["slack_token"]
    openai_api_key = config["openai_api_key"]
    text_method = config['text_method']
    agent = PDFQuestionAnsweringAgent(
        pdf_path=pdf_path,
        questions=questions,
        slack_channel=slack_channel,
        slack_token=slack_token,
        api_key=openai_api_key,
        text_method=text_method
    )
    agent.run()
    print(f'All state is completed successfully .....')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Question Answering Agent")
    parser.add_argument('--config_path',required=True, type=str, help="Path to the configuration file")
    args = parser.parse_args()
    main(args.config_path)
    
    
'''
How to run the scripts

python3 main.py --config_path config.yaml

'''
