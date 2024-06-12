# LLM-and-RAG-Enabled-Slack-Bot-for-Document-Insights

## Introduction
The **LLM-and-RAG-Enabled-Slack-Bot-for-Document-Insights** is a powerful tool designed to extract meaningful insights from documents using advanced technologies like Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG). LLMs are AI models trained on vast amounts of text data, capable of understanding and generating human-like text. RAG combines the strengths of LLMs with efficient retrieval mechanisms, enhancing the bot's ability to provide accurate and contextually relevant answers from large documents.

## Approach/Solutions
Our solution offers multiple approaches to handle document insights:

### a. Text Approach
In this method, the entire text of the document is sent to the LLM along with the user's question. This approach works well for small documents but can hit token limits with larger texts, potentially leading to incomplete or erroneous responses.

### b. Page Approach
Given the token limitations of LLMs, sending the entire document at once is impractical for large files. Instead, this approach processes the document page by page, sending each page to the LLM along with the question. This method ensures that we stay within token limits but can be less efficient if the information is spread across multiple pages.

### c. Chunk Approach
Similar to the page approach, the chunk approach divides the document into smaller parts based on token count rather than pages. For example, if the token limit is 1000, the document is split into chunks of 1000 tokens. This method provides more control over the size of the text being processed, ensuring optimal use of the LLM's capacity.

### d. RAG Approach
In the RAG approach, embeddings for each page are generated and stored. When a question is asked, the embeddings are used to identify the top 2 most relevant pages, which are then sent to the LLM along with the question. This method is more efficient and cost-effective, as it reduces the amount of text processed by the LLM, staying well within token limits and minimizing costs. For example, if each page embedding costs a certain amount and processing two pages costs less than processing the entire document, RAG significantly cuts down on expenses while maintaining high accuracy.

## Code Pattern/Architecture
The implementation uses a state machine approach, comprising three main states:

1. **PDF Extractor**: Extracts text from PDF documents.
2. **OpenAI Response**: Sends text chunks to the LLM and retrieves responses.
3. **Slack Client**: Integrates with Slack to allow user interaction and display responses.

This state machine architecture is robust and suitable for production-level applications due to its clear separation of concerns, ease of maintenance, and scalability.

## Environment Setup
To set up the environment, use the following commands:

```sh
conda create -n env python=3.10
conda activate env
pip install -r requirements.txt
```

## Configuration Setup
A YAML configuration file is used to provide necessary values. Ensure to update the `config.yaml` file with appropriate settings such as API keys, document paths, and Slack credentials.

## Usage
To run the script, execute the `main.py` file:

```sh
python main.py --config_file config.yaml
```


By following this README, users can set up and utilize the **LLM-and-RAG-Enabled-Slack-Bot-for-Document-Insights** efficiently, leveraging advanced AI capabilities to extract valuable insights from documents seamlessly.
