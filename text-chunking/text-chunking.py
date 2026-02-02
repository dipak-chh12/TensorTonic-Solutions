def text_chunking(tokens, chunk_size, overlap):
    chunks = []
    step = chunk_size - overlap
    n = len(tokens)

    i = 0
    while i < n:
        chunk = tokens[i:i + chunk_size]
        if not chunk:
            break
        # avoid producing a final chunk that adds no new tokens
        if chunks and len(chunk) <= overlap:
            break
        chunks.append(chunk)
        i += step

    return chunks
