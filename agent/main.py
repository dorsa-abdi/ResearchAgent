import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("pipeline.py"), '..')))

from agent.pipeline import run_pipeline

def main():
    user_input = input("Enter your research interest: ")
    results = run_pipeline(user_input)
    
    for i, r in enumerate(results, 1):
        print(f"\n{i}. {r['title']} ({r['year']})\n{r['authors']}\n{r['link']}\n")

if __name__ == "__main__":
    main()