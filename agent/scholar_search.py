from scholarly import scholarly

def search_google_scholar(keywords, num_results=5):
    query = " ".join(keywords)
    search = scholarly.search_pubs(query)
    results = []

    for _ in range(num_results):
        try:
            pub = next(search)
            bib = pub['bib']
            authors = bib.get('author', 'Unknown Author')
            title = bib.get('title', 'No title')
            year = bib.get('pub_year', 'n.d.')
            url = pub.get('pub_url', 'N/A')

            citation = f"{authors} ({year}). *{title}*. Retrieved from {url}"

            results.append({
                "title": title,
                "author": authors,
                "year": year,
                "url": url,
                "citation": citation
            })
        except StopIteration:
            break
        except Exception as e:
            print("Error retrieving publication:", e)
            continue

    return results