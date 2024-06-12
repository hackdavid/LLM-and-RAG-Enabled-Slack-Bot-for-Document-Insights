
from typing import List,Tuple
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

class TextMethod:
    
    @classmethod
    def get_text(cls,text:List) -> List:
        return [' '.join(text)]

class ChunkMethod:
    
    @classmethod
    def get_text(cls,text:List) -> List:
        # first make a single text by joining each page text 
        text = ' '.join(text)
        words = text.split()
        max_tokens = 2000
        chunks = []
        current_chunk = []
        current_length = 0
        for word in words:
            current_length += len(word) + 1
            if current_length > max_tokens:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_length = len(word) + 1
            current_chunk.append(word)
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        return chunks
    
class PageWiseChunkMethod:
    
    @classmethod
    def get_text(cls,text:List) -> List:
        return text
    
class RagMethod:
    _documents = []
    _vectorstore = None
    
    @classmethod
    def prepare_vector_document(cls,text,api_key):
        '''
        this is create new vector database using chorma which is in memory 
        Also use openai embedding model to get text embedding
        '''
        for i,page_text in enumerate(text):
           cls._documents.append(Document(
                page_content=page_text,
                metadata={"source": f"page_number_{i+1}"},
            ))
        cls._vectorstore = Chroma.from_documents(cls._documents,embedding=OpenAIEmbeddings(openai_api_key=api_key),)
    
    @classmethod
    def get_text(cls,text:List,question:str,api_key:str) -> List:
        if not cls._documents:
            cls.prepare_vector_document(text,api_key)
        result = cls._vectorstore.similarity_search(question,k=2)
        text = []
        for item in result:
            text.append(item.page_content)
        return text


class TextFactory:
    _text_method_map = {
        'text': TextMethod,
        'chunk': ChunkMethod,
        'page': PageWiseChunkMethod,
        'rag': RagMethod
    }
    
    @classmethod
    def get(cls,choice):
        return cls._text_method_map[choice]