from Scripts.tools import use_tool

def agent(query, context=None):
    """
    Routes the query to the appropriate tool or LLM.
    For LLM QA, context is required.
    """
    q = query.lower()
    if "translate" in q:
        return use_tool("translate", query)
    elif "pubmed" in q or "medical" in q or "disease" in q:
        return use_tool("pubmed", query)
    elif "vector" in q or "retrieve" in q or "document" in q:
        # RAG: Retrieve context from vector db, then answer with LLM
        from Scripts.vector_db import retrieve
        from Scripts.large_llm import ask_llm
        context = retrieve(query, top_k=1)[0]
        return ask_llm(query, context)
    else:
        # Default: Use LLM (fine-tuned or distilled)
        from Scripts.large_llm import ask_llm
        if context is None:
            # Default context, or you can prompt user for context
            context = "The Colossus of Rhodes was a statue of the Greek sun-god Helios, erected in the city of Rhodes by Chares of Lindos in 280 BC."
        return ask_llm(query, context)

if __name__ == "__main__":
    print(agent("Translate this to Korean: Hello!"))
    print(agent("PubMed: heart disease latest studies"))
    print(agent("Retrieve: Who built the Colossus of Rhodes?"))
    print(agent("Who built the Colossus of Rhodes?",
        "The Colossus of Rhodes was a statue of the Greek sun-god Helios, erected in the city of Rhodes by Chares of Lindos in 280 BC."))
