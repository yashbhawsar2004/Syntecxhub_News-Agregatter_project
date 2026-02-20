def filter_by_keyword(articles, keyword):
    if not keyword:
        return articles
    return [a for a in articles if keyword.lower() in a["title"].lower()]


def filter_by_source(articles, source):
    if not source:
        return articles
    return [a for a in articles if source.lower() in a["source"].lower()]


def filter_by_date(articles, date):
    if not date:
        return articles
    return [a for a in articles if a["date"] == date]