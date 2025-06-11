import requests

def search_pubmed(query, max_results=3):
    """
    Search PubMed for the given query and return a list of article titles.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    resp = requests.get(base_url, params=params)
    resp.raise_for_status()
    ids = resp.json()["esearchresult"]["idlist"]

    if not ids:
        return "No PubMed results found."

    # Fetch summaries for the found IDs
    summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    summary_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "json"
    }
    summary_resp = requests.get(summary_url, params=summary_params)
    summary_resp.raise_for_status()
    summaries = summary_resp.json()["result"]

    # Collect titles
    titles = []
    for pid in ids:
        title = summaries[pid].get("title", "No title")
        titles.append(title)

    return "\n".join(titles)