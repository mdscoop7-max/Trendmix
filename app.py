from flask import Flask, render_template
import json
import os

app = Flask(__name__)


# ---------------------------------------------------------
# Homepage
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------------------------
# Categoriepagina
# ---------------------------------------------------------

@app.route("/<category>")
def category_page(category):

    allowed_categories = [
        "pc-componenten",
        "gadgets",
        "smart-home",
        "beauty-care",
        "lifestyle-sport",
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

    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return "Productbestand kan niet worden gelezen", 500

    products = data.get("products", [])

    # -----------------------------------------------------
    # Productafbeeldingen voorbereiden
    # -----------------------------------------------------

    for product in products:

        image = str(product.get("image", "")).strip()

        if image:
            product["image_url"] = image
        else:
            product["image_url"] = ""

    return render_template(
        "category.html",
        category=data.get("category", category),
        products=products
    )


# ---------------------------------------------------------
# Start Flask
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)