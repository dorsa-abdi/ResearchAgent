import os
import random
import itertools
import arxiv

def generate_random_subsets(keywords, max_queries=2):
    all_subsets = []
    for r in range(1, len(keywords) + 1):
        subsets = list(itertools.combinations(keywords, r))
        all_subsets.extend(subsets)
    return random.sample(all_subsets, min(max_queries, len(all_subsets)))

def search_arxiv_with_keywords(keywords, num_results=8, max_queries=2):
    subsets = generate_random_subsets(keywords, max_queries)
    all_results = []

    for subset in subsets:
        query = " ".join(subset)
        print(f"Searching arXiv for: {query}")

        try:
            results = arxiv.Search(
                query=query,
                max_results=num_results,
                sort_by=arxiv.SortCriterion.Relevance
            )

            for paper in results.results():
                all_results.append({
                    "title": paper.title,
                    "authors": ", ".join([a.name for a in paper.authors]),
                    "year": paper.published.date().year,
                    "link": paper.entry_id,
                    "summary": paper.summary
                })
        except Exception as e:
            print(f"Error during arXiv search: {e}")
            continue

    return all_results