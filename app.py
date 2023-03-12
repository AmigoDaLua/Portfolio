from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit Tracking app with Python & MongoDB",
        "thumb": "img/habit2.png", 
        "hero": "img/habit2.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-b4cw.onrender.com/"
    },
        {
        "name": "Movie Watchlist app with Flask & MongoDB",
        "thumb": "img/gojira.png",
        "hero": "img/gojira.png",
        "categories": ["Flask", "MongoDB", "web"],
        "slug": "movies-watchlist",
        "prod": "https://movies-watchlist-7dwn.onrender.com/"
    },
        {
        "name": "Book Recommendation app with Python & SQL",
        "thumb": "img/libreria.png",
        "hero": "img/libreria.png",
        "categories": ["flask", "SQL", "web"],
        "slug": "book-rex",
        "prod": "https://book-rex.onrender.com/"
    }
]

slug_to_project = {project['slug']: project for project in projects}
# LIST COMPREHEENSION que usa as SLUGS pra mapear os dicionários inteiros
# e assim permite "criar um índice" pra navegar na coisa toda melhor!

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
        
    return render_template(f"project_{slug}.html", 
                            project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404