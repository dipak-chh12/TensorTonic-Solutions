def remove_stopwords(tokens, stopwords):
    stopwords = {
        "the","a","an","is","are","was","were",
        "in","on","at","to","for","of","and","or","it"
    }
    res = []
    for token in tokens:
        if token not in stopwords:
            res.append(token)
    return res
