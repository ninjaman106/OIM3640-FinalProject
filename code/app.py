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


"This file initializes the Flask web server and defines the main route for the application. "
"When a user submits their interests through the form, the app retrieves news articles "
"from the news API and passes them to the recommendation engine. The results are then "
"displayed back to the user on the webpage. This file acts as the central hub that coordinates "
"data flow between the user interface"