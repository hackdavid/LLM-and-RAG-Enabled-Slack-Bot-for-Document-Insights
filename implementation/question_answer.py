# components/question_answerer.py
from openai import OpenAI
from .text_factory import TextFactory

class QuestionAnswerer:
    
    @classmethod
    def process(cls,api_key,choice,text,questions):
        client = OpenAI(
            api_key=api_key,
        )
        answers = {question: [] for question in questions}
        for question in questions:
            if choice == 'rag':
                chunks = TextFactory.get(choice).get_text(text,question,api_key)
                chunks = ' '.join(chunks)
                ans = cls.openai_response(client,question,chunks)
                answers[question].append(ans)
            else:
                chunks = TextFactory.get(choice).get_text(text)
                for chunk in chunks:
                    ans = cls.openai_response(client,question,chunk)
                    answers[question].append(ans)
        final_answers = {}
        for question, answer_list in answers.items():
            combined_answer = ' '.join(answer_list)
            if "I'm sorry" in combined_answer or "I don't know" in combined_answer:
                final_answers[question] = "Data Not Available"
            else:
                final_answers[question] = combined_answer
        
        return final_answers
    
    
    @classmethod
    def openai_response(cls,client,question,text):
        system_prompt = """
        You are a highly knowledgeable and accurate assistant. Answer the questions based on the provided text.
        If you are unsure or do not have enough information to answer a question, respond with "I don't know."
        Do not attempt to provide an answer if you are not certain.
        """
        user_prompt = f"""
        Based on the following text, answer the question:

        Text: {text}

        Question: {question}

        If you are unsure or do not have enough information to answer, respond with "I don't know."
        """
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
        )
        answer = response.choices[0].message.content.strip()
        return answer
        
