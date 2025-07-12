from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
api =  os.getenv("GROQ_API")




llm = ChatGroq(
    temperature=0.3,
    model_name="llama-3.1-8b-instant",
    api_key=api
)


extract_prompt = PromptTemplate.from_template("""
Given this research interest: "{research_text}"
key technical keywords from it in a comma-separated list. just give the list of essensial keywords and nothing more. 
""")

extract_chain = extract_prompt | llm

def extract_keywords(text):
    result = extract_chain.invoke(input={"research_text": text})
    result_text = result.content  
    return [kw.strip() for kw in result_text.split(",")]

