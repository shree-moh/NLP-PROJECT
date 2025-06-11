def use_tool(tool_name, query):
    if tool_name == "translate":
        from Scripts.translate import translate_en_to_ko
        return translate_en_to_ko(query)
    elif tool_name == "pubmed":
        from Scripts.pubmed_api import search_pubmed
        return search_pubmed(query)
    else:
        return "Tool not found."