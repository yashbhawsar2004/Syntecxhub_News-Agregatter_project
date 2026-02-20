def remove_duplicates(articles):
    seen = set()
    unique_articles = []

    for article in articles:
        identifier = article["title"] + article["date"]

        if identifier not in seen:
            seen.add(identifier)
            unique_articles.append(article)

    return unique_articles