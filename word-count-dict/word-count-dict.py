def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    freq = {}
    for sentence in sentences:
        for token in sentence:
            freq[token] = freq.get(token, 0) + 1
    return freq