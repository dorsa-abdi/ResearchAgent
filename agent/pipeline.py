import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("keyword_expander.py"), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("keyword_extractor.py"), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("scholar_search.py"), '..')))
from agent.keyword_extractor import extract_keywords
from agent.keyword_expander import expand_keywords
from agent.scholar_search import search_google_scholar

def run_pipeline(user_input):
    base_keywords = extract_keywords(user_input)
    
    enriched_keywords = expand_keywords(base_keywords)
    
    final_keywords = base_keywords + enriched_keywords
    results = search_google_scholar(final_keywords[:8])
    return results