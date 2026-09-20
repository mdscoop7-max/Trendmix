import json
import re
import os
import urllib.request
import urllib.error
from pathlib import Path
from flask import Flask, Response, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'trendmix-cart-secret-change-me')
BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_DIR = BASE_DIR / "products"
SITE_URL = "https://trendmix.onrender.com"

CATEGORIES = {
    "pc-componenten": {"name": "PC-Componenten", "icon": "🖥️", "eyebrow": "Performance & gaming"},
    "gadgets": {"name": "Gadgets", "icon": "⚡", "eyebrow": "Slimme tech voor elke dag"},
    "smart-home": {"name": "Smart Home", "icon": "🏠", "eyebrow": "Comfort & connected living"},
    "beauty-care": {"name": "Beauty & Care", "icon": "✨", "eyebrow": "Self-care & beauty"},
    "lifestyle-sport": {"name": "Sport & Lifestyle", "icon": "🏃", "eyebrow": "Move, recover & live"},
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
        product.setdefault("cost_price", 0)
        product.setdefault("margin", 0)
        product.setdefault("orders", 0)
        cleaned.append(product)
    return cleaned


def load_catalog():
    catalog = {}
    global_seen = set()
    for slug in CATEGORIES:
        path = PRODUCTS_DIR / slug / "products.json"
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            items = clean_products(data.get("products", []))
            unique_items = []
            for item in items:
                key = item["name"].casefold()
                if key in global_seen:
                    continue
                global_seen.add(key)
                unique_items.append(item)
            catalog[slug] = unique_items
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            catalog[slug] = []
    return catalog


products = load_catalog()


def catalog_items():
    for slug, items in products.items():
        for index, product in enumerate(items):
            item = dict(product)
            item["category_slug"] = slug
            item["category_name"] = CATEGORIES[slug]["name"]
            item["index"] = index
            yield item


def featured_mix():
    mixed = []
    for index in range(4):
        for slug in CATEGORIES:
            items = products.get(slug, [])
            if index < len(items):
                item = dict(items[index])
                item["category_slug"] = slug
                item["category_name"] = CATEGORIES[slug]["name"]
                item["index"] = index
                mixed.append(item)
            if len(mixed) >= 10:
                return mixed
    return mixed


def category_images():
    return {slug: (items[0].get("image", "") if items else "") for slug, items in products.items()}


def slugify(value):
    value = re.sub(r"[^a-zA-Z0-9\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def cart_items():
    return session.get("trendmix_cart", [])


def cart_count():
    return sum(max(1, int(item.get("qty", 1))) for item in cart_items())


def cart_total():
    return sum(
        float(item.get("price", 0) or 0) * max(1, int(item.get("qty", 1)))
        for item in cart_items()
    )


def find_product(product_id):
    try:
        category_slug, raw_index = product_id.rsplit("-", 1)
        index = int(raw_index)
    except (ValueError, TypeError):
        return None
    if category_slug not in products or index < 0 or index >= len(products[category_slug]):
        return None
    product = dict(products[category_slug][index])
    product["id"] = product_id
    product["category_slug"] = category_slug
    product["category_name"] = CATEGORIES[category_slug]["name"]
    product["index"] = index
    return product


@app.context_processor
def inject_helpers():
    return {"slugify": slugify, "cart_count": cart_count()}




@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    all_items = list(catalog_items())
    search_results = []
    if query:
        needle = query.casefold()
        search_results = [item for item in all_items if needle in item["name"].casefold() or needle in item["category_name"].casefold()]
    counts = {slug: len(items) for slug, items in products.items()}
    return render_template("index.html", categories=CATEGORIES, featured_products=featured_mix(), category_images=category_images(), search_query=query, search_results=search_results, counts=counts, total_products=len(all_items))


INFO_PAGES = {
    "over-trendmix": {"title": "Over TrendMix", "description": "Informatie over TrendMix als webshop.", "content": """
        <p>TrendMix is een moderne webshop voor geselecteerde producten in tech, home, beauty en lifestyle. Je kunt producten bekijken, aan je winkelwagen toevoegen en rechtstreeks via TrendMix bestellen.</p>
        <h2>Onze webshop</h2>
        <p>TrendMix toont productinformatie, prijzen en beschikbaarheid zodat je eenvoudig kunt kiezen en bestellen.</p>
        <h2>Klantenservice</h2>
        <p>Heb je een vraag over een product of bestelling? Gebruik het contactformulier in de footer.</p>
        """},
    "bestellen": {"title": "Bestellen & levering", "description": "Informatie over bestellen, betalen, levering en retouren bij TrendMix.", "content": """
        <p>Je bestelt rechtstreeks via TrendMix. Voeg een product toe aan je winkelwagen en volg de stappen tijdens het afrekenen.</p>
        <h2>Betaling</h2>
        <p>De beschikbare betaalmethode wordt tijdens het afrekenen getoond. Controleer je bestelling voordat je de betaling bevestigt.</p>
        <h2>Levering</h2>
        <p>Na betaling wordt je bestelling verwerkt en verzonden naar het opgegeven afleveradres. De actuele levertijd wordt bij het product of tijdens het afrekenen vermeld.</p>
        <h2>Retouren</h2>
        <p>Voor retouren gelden de retourvoorwaarden van TrendMix. Neem bij vragen contact op met onze klantenservice.</p>
        """},
    "privacy": {"title": "Privacy", "description": "Privacyinformatie voor klanten en bezoekers van TrendMix.", "content": """
        <p>TrendMix verwerkt gegevens die nodig zijn om bestellingen uit te voeren, betalingen te verwerken, producten te leveren en klantenservice te bieden.</p>
        <h2>Taalvoorkeur</h2>
        <p>De gekozen taal kan lokaal in je browser worden opgeslagen zodat TrendMix je voorkeur bij een volgend bezoek kan onthouden.</p>
        <h2>Externe diensten</h2>
        <p>Voor betaling, verzending en technische dienstverlening kunnen externe dienstverleners worden gebruikt.</p>
        <h2>Wijzigingen</h2>
        <p>Deze informatie kan worden aangepast wanneer de functies van TrendMix veranderen.</p>
        """},
    "cookies": {"title": "Cookies & voorkeuren", "description": "Informatie over cookies en voorkeuren bij TrendMix.", "content": """
        <p>TrendMix gebruikt lokale opslag voor instellingen zoals je taalvoorkeur. Dit helpt de webshop je voorkeur te onthouden.</p>
        <h2>Functionele opslag</h2>
        <p>Winkelwagengegevens en taalvoorkeuren kunnen lokaal in je browser worden bewaard om de webshop goed te laten werken.</p>
        <h2>Voorkeur wissen</h2>
        <p>Je kunt lokale sitegegevens in de instellingen van je browser wissen.</p>
        """},
}



def render_info_page(info_slug):
    page = INFO_PAGES.get(info_slug)
    if not page:
        return "Pagina niet gevonden", 404
    return render_template("info.html", title=page["title"], description=page["description"], info_slug=info_slug, path=f"/{info_slug}", content=page["content"], categories=CATEGORIES)


@app.route("/<category_slug>")
def category_page(category_slug):
    if category_slug not in CATEGORIES:
        return "Pagina niet gevonden", 404
    category = CATEGORIES[category_slug]
    category_products = []
    for index, item in enumerate(products[category_slug]):
        category_item = dict(item)
        category_item["category_slug"] = category_slug
        category_item["category_name"] = category["name"]
        category_item["index"] = index
        category_products.append(category_item)
    return render_template("category.html", category_name=category["name"], category_icon=category["icon"], category_eyebrow=category["eyebrow"], category_slug=category_slug, categories=CATEGORIES, products=category_products)


@app.route("/product/<category_slug>/<int:product_index>")
def product_detail(category_slug, product_index):
    if category_slug not in products or product_index < 0 or product_index >= len(products[category_slug]):
        return "Product niet gevonden", 404
    product = dict(products[category_slug][product_index])
    product["category_slug"] = category_slug
    product["category_name"] = CATEGORIES[category_slug]["name"]
    product["index"] = product_index
    related = []
    for index, item in enumerate(products[category_slug][:6]):
        related_item = dict(item)
        related_item["category_slug"] = category_slug
        related_item["category_name"] = CATEGORIES[category_slug]["name"]
        related_item["index"] = index
        related.append(related_item)
    return render_template("product.html", product=product, product_index=product_index, category_slug=category_slug, category_name=CATEGORIES[category_slug]["name"], categories=CATEGORIES, related=related)


@app.route("/winkelwagen", methods=["GET", "POST"])
def winkelwagen():
    cart = [dict(item) for item in cart_items()]

    if request.method == "POST":
        action = request.form.get("action", "").strip()

        if action == "add":
            product = find_product(request.form.get("product_id", "").strip())
            if product:
                found = next((item for item in cart if item["id"] == product["id"]), None)
                if found:
                    found["qty"] = max(1, int(found.get("qty", 1))) + 1
                else:
                    cart.append({
                        "id": product["id"],
                        "name": product["name"],
                        "price": float(product.get("price", 0) or 0),
                        "image": product.get("image", ""),
                        "category_name": product["category_name"],
                        "qty": 1,
                    })

        elif action == "change":
            product_id = request.form.get("product_id", "").strip()
            try:
                delta = int(request.form.get("delta", "0"))
            except ValueError:
                delta = 0
            for item in cart:
                if item.get("id") == product_id:
                    item["qty"] = max(1, int(item.get("qty", 1)) + delta)
                    break

        elif action == "remove":
            product_id = request.form.get("product_id", "").strip()
            cart = [item for item in cart if item.get("id") != product_id]

        elif action == "clear":
            cart = []

        session["trendmix_cart"] = cart
        session.modified = True
        return redirect(url_for("winkelwagen"))

    total = sum(
        float(item.get("price", 0) or 0) * max(1, int(item.get("qty", 1)))
        for item in cart
    )
    return render_template(
        "cart.html",
        categories=CATEGORIES,
        cart=cart,
        cart_count=cart_count(),
        cart_total=total,
    )


@app.route("/afrekenen")
def afrekenen():
    cart = [dict(item) for item in cart_items()]
    if not cart:
        return redirect(url_for("winkelwagen"))
    total = sum(
        float(item.get("price", 0) or 0) * max(1, int(item.get("qty", 1)))
        for item in cart
    )
    return render_template(
        "checkout.html",
        categories=CATEGORIES,
        cart=cart,
        cart_count=cart_count(),
        cart_total=total,
    )


@app.route("/faq")
def faq():
    return render_template("faq.html", categories=CATEGORIES)

@app.route("/contact", methods=["GET"])\ndef contact_page():\n    return render_template("contact.html", categories=CATEGORIES, search_query="")\n\n@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message or len(name) > 120 or len(email) > 254 or len(message) > 5000:
        return redirect(url_for("home") + "?contact=error#contact")

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return redirect(url_for("home") + "?contact=error#contact")

    is_ajax = request.args.get("ajax") == "1" or request.headers.get("X-Requested-With") == "XMLHttpRequest"
    api_key = os.getenv("RESEND_API_KEY")
    from_email = os.getenv("CONTACT_FROM_EMAIL")

    # Testvriendelijk: zonder mailconfiguratie accepteren we het formulier alsnog.
    # Zo kan de volledige gebruikersflow op Vercel worden getest zonder dat e-mail al is gekoppeld.
    if not api_key or not from_email:
        app.logger.info("Contact test submission received from %s <%s>: %s", name, email, message)
        if is_ajax:
            return Response(json.dumps({"ok": True, "test_mode": True}), mimetype="application/json")
        return redirect(url_for("home") + "?contact=sent#contact")

    payload = {
        "from": from_email,
        "to": ["mdscoop020@gmail.com"],
        "reply_to": email,
        "subject": f"TrendMix contactformulier: {name}",
        "text": f"Naam: {name}\\nE-mail: {email}\\n\\nBericht:\\n{message}",
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if 200 <= response.status < 300:
                if is_ajax:
                    return Response(json.dumps({"ok": True}), mimetype="application/json")
                return redirect(url_for("home") + "?contact=sent#contact")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        app.logger.error("Contact mail failed: %s", exc)

    if is_ajax:
        return Response(json.dumps({"ok": False}), status=502, mimetype="application/json")
    return redirect(url_for("home") + "?contact=error#contact")

@app.route("/over-trendmix")
def over_trendmix():
    return render_info_page("over-trendmix")


@app.route("/bestellen")
def bestellen():
    return render_info_page("bestellen")


@app.route("/privacy")
def privacy():
    return render_info_page("privacy")


@app.route("/cookies")
def cookies():
    return render_info_page("cookies")


@app.route("/robots.txt")
def robots():
    return Response(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{slug}" for slug in CATEGORIES] + [f"{SITE_URL}/{path}" for path in INFO_PAGES] + [f"{SITE_URL}/faq"]
    for slug, items in products.items():
        for index, _product in enumerate(items):
            urls.append(f"{SITE_URL}/product/{slug}/{index}")
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" + "".join(f"<url><loc>{url}</loc></url>" for url in urls) + "</urlset>"
    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
