def score_article(article, interests):
    text = f"{article['title']} {article.get('description', '')}".lower()
    score = 0

    for interest in interests:
        if interest.strip().lower() in text:
            score += 1

    return score


def recommend(articles, interests):
    scored = []

    for article in articles:
        score = score_article(article, interests)
        if score > 0:
            scored.append((article, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:5]


"file analyzes each news article and compares it to the user’s "
"stated interests. It uses simple keyword matching to assign a relevance "
"score to each article based on how many times user interests appear in the article’s "
"title or description."