from langchain_community.chat_models import Ollam
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import StrOutputParser
import logging

logging.basicConfig(level=logging.DEBUG

def initialize_llama3():

    try:
    create_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a CBT Therapist assistant."),
            ("user", "Statement: {input}"),
        ]
    )

    llama_model = Ollama(model = "llama3")
    format_output = StrOutputParser()

    chain = create_prompt | llama_model | format_output

    return chain
    except Exception as e:
        logging.error(f"Error initializing Llama3: {e}")
        raise
    chain = initialize_llama3()

    def main(): 