from flask import Flask, render_template, request
from news_api import get_articles
from recommender import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        interests = request.form["interests"].split(",")
        articles = get_articles()
        recommendations = recommend(articles, interests)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
