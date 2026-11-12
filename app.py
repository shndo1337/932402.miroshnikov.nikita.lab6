from flask import Flask, jsonify, request

app = Flask(__name__, static_folder="public", static_url_path="")

BOOKS = [
    {"title": "Война и мир", "author": "Tolstoy", "year": 1869},
    {"title": "Анна Каренина", "author": "Tolstoy", "year": 1877},
    {"title": "Преступление и наказание", "author": "Dostoevsky", "year": 1866},
    {"title": "Идиот", "author": "Dostoevsky", "year": 1869},
    {"title": "Мастер и Маргарита", "author": "Bulgakov", "year": 1967},
    {"title": "Евгений Онегин", "author": "Pushkin", "year": 1833},
]


@app.get("/")
def index():
    return app.send_static_file("index.html")


@app.get("/about")
def about():
    return app.send_static_file("about.html")


@app.get("/api/books")
def books():
    author = request.args.get("author")
    year = request.args.get("year")
    result = BOOKS

    if author:
        result = [b for b in result if b["author"].lower() == author.lower()]
    if year:
        result = [b for b in result if str(b["year"]) == year]

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=3000)