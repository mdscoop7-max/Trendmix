import json
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_DIR = BASE_DIR / "products"

CATEGORIES = {
    "pc-componenten": {"name": "PC-Componenten", "icon": "🖥️"},
    "gadgets": {"name": "Gadgets", "icon": "🔌"},
    "smart-home": {"name": "Smart Home", "icon": "🏠"},
    "beauty-care": {"name": "Beauty & Care", "icon": "✨"},
    "lifestyle-sport": {"name": "Sport & Lifestyle", "icon": "🏃"},
}


def clean_products(items):
    cleaned = []
    seen = set()
    for raw in items:
        name = str(raw.get("name", "")).strip()
        if not name:
            continue
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        product = dict(raw)
        product.setdefault("image", "")
        product.setdefault("icon", "🛍️")
        product.setdefault("price", 0)
        cleaned.append(product)
    return cleaned


def load_catalog():
    catalog = {}
    for slug in CATEGORIES:
        path = PRODUCTS_DIR / slug / "products.json"
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            catalog[slug] = clean_products(data.get("products", []))
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            catalog[slug] = []
    return catalog


products = load_catalog()


def catalog_items():
    for slug, items in products.items():
        for product in items:
            item = dict(product)
            item["category_slug"] = slug
            item["category_name"] = CATEGORIES[slug]["name"]
            yield item


@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    all_items = list(catalog_items())
    search_results = []

    if query:
        needle = query.casefold()
        search_results = [
            item for item in all_items
            if needle in item["name"].casefold()
        ]

    popular_products = []
    for slug in CATEGORIES:
        popular_products.extend(products[slug][:2])

    return render_template(
        "index.html",
        categories=CATEGORIES,
        popular_products=popular_products,
        search_query=query,
        search_results=search_results,
    )


@app.route("/<category_slug>")
def category_page(category_slug):
    if category_slug not in CATEGORIES:
        return "Pagina niet gevonden", 404

    category = CATEGORIES[category_slug]
    return render_template(
        "category.html",
        category_name=category["name"],
        category_icon=category["icon"],
        category_slug=category_slug,
        categories=CATEGORIES,
        products=products[category_slug],
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
