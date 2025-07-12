import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("keyword_expander.py"), '..')))

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from agent.keyword_extractor import llm


expand_prompt = PromptTemplate.from_template("""
Given these keywords: {keywords}
Add 3–5 related academic keywords. Return them as a comma-separated list. just output the keywords and nothingmore
""")

expand_chain = expand_prompt | llm

def expand_keywords(keywords):
    joined = ", ".join(keywords)
    result = expand_chain.invoke(input={"keywords": joined})
    result_text = result.content 
    return [kw.strip() for kw in result_text.split(",")]

