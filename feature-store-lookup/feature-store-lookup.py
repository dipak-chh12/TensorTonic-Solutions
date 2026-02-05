def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    result = []

    for req in requests:
        user_id = req.get("user_id")
        online_features = req.get("online_features", {})

        # start with defaults
        merged = dict(defaults)

        # merge offline features if user exists
        if user_id in feature_store:
            merged.update(feature_store[user_id])

        # merge online (request-time) features
        merged.update(online_features)

        result.append(merged)

    return result
