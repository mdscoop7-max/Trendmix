from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<category>")
def category_page(category):

    allowed_categories = [
        "pc-componenten",
        "gadgets",
        "cosmetica",
        "keuken",
        "handige-producten",
        "aanbiedingen"
    ]

    if category not in allowed_categories:
        return "Categorie niet gevonden", 404

    file_path = os.path.join(
        "products",
        category,
        "products.json"
    )

    if not os.path.exists(file_path):
        return "Productbestand niet gevonden", 404

    with open(file_path, "r", encoding="utf-8-sig") as file:
        data = json.load(file)

    return render_template(
        "category.html",
        category=data["category"],
        products=data["products"]
    )


if __name__ == "__main__":
    app.run(debug=True)

