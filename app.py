import json
import re
import os
import urllib.request
import urllib.error
from pathlib import Path
from flask import Flask, Response, render_template, request, redirect, url_for

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_DIR = BASE_DIR / "products"
SITE_URL = "https://trendmix-jet.vercel.app"

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


@app.context_processor
def inject_helpers():
    return {"slugify": slugify}


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
    "over-trendmix": {"title": "Over TrendMix", "description": "Hoe TrendMix werkt als onafhankelijke productcatalogus.", "content": """
        <p>TrendMix is een onafhankelijke productcatalogus voor moderne trends in tech, home, beauty en lifestyle. We brengen producten overzichtelijk samen zodat je sneller kunt ontdekken wat interessant is.</p>
        <h2>Geen gewone webshop</h2>
        <p>TrendMix is ingericht als discovery- en affiliateplatform. Een aankoop wordt niet bij TrendMix afgerekend: wanneer je op een productdoorgang klikt, kun je worden doorgestuurd naar een externe aanbieder.</p>
        <h2>Prijzen en beschikbaarheid</h2>
        <p>Productprijzen, voorraad, levering en voorwaarden kunnen veranderen. Controleer daarom altijd de actuele informatie bij de externe aanbieder voordat je bestelt.</p>
        """},
    "affiliate": {"title": "Affiliate & transparantie", "description": "Transparantie over affiliate links en commerciële relaties bij TrendMix.", "content": """
        <p><strong>TrendMix kan affiliate links gebruiken.</strong> Als je via zo’n link bij een externe aanbieder een aankoop doet, kan TrendMix daarvoor een commissie ontvangen. De commissie verandert jouw prijs niet.</p>
        <h2>Waarom melden we dit?</h2>
        <p>We willen duidelijk maken wanneer een productdoorgang commercieel kan zijn. Reclame en commerciële relaties horen herkenbaar en transparant te zijn.</p>
        <h2>Onze productinformatie</h2>
        <p>TrendMix gebruikt catalogusinformatie om producten te presenteren. Controleer voor aankoop altijd de actuele prijs, voorraad, specificaties, levering en retourvoorwaarden bij de aanbieder.</p>
        <h2>Reviews</h2>
        <p>TrendMix presenteert geen verzonnen reviews of beoordelingen. Wanneer er in de toekomst externe beoordelingen worden getoond, moet duidelijk zijn waar deze vandaan komen.</p>
        """},
    "privacy": {"title": "Privacy", "description": "Privacyinformatie voor bezoekers van TrendMix.", "content": """
        <p>TrendMix is opgezet als een eenvoudige productcatalogus. We vragen op dit moment geen account aan om de catalogus te bekijken.</p>
        <h2>Taalvoorkeur</h2>
        <p>De gekozen taal kan lokaal in je browser worden opgeslagen zodat TrendMix je voorkeur bij een volgend bezoek kan onthouden.</p>
        <h2>Externe aanbieders</h2>
        <p>Wanneer je TrendMix verlaat via een product- of affiliate link, geldt het privacybeleid van de externe website die je bezoekt. Lees daar de voorwaarden voordat je gegevens achterlaat of een aankoop doet.</p>
        <h2>Wijzigingen</h2>
        <p>Deze informatie kan worden aangepast wanneer de functies van TrendMix veranderen.</p>
        """},
    "cookies": {"title": "Cookies & voorkeuren", "description": "Informatie over cookies en lokale voorkeuren op TrendMix.", "content": """
        <p>TrendMix houdt de site bewust eenvoudig. De huidige taalkeuze kan lokaal in je browser worden bewaard. Dit is een lokale voorkeur en geen TrendMix-account.</p>
        <h2>Externe websites</h2>
        <p>Externe aanbieders kunnen hun eigen cookies, analytics of advertentietechnieken gebruiken nadat je TrendMix verlaat. Controleer daarvoor het cookie- en privacybeleid van die aanbieder.</p>
        <h2>Voorkeur wissen</h2>
        <p>Je kunt lokale sitegegevens in de instellingen van je browser wissen. Daarna wordt de standaardtaal opnieuw gebruikt.</p>
        """},
}


def render_info_page(info_slug):
    page = INFO_PAGES.get(info_slug)
    if not page:
        return "Pagina niet gevonden", 404
    return render_template("info.html", title=page["title"], description=page["description"], info_slug=info_slug, path=f"/{info_slug}", categories=CATEGORIES)


@app.route("/<category_slug>")
def category_page(category_slug):
    if category_slug not in CATEGORIES:
        return "Pagina niet gevonden", 404
    category = CATEGORIES[category_slug]
    return render_template("category.html", category_name=category["name"], category_icon=category["icon"], category_eyebrow=category["eyebrow"], category_slug=category_slug, categories=CATEGORIES, products=products[category_slug])


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


@app.route("/faq")
def faq():
    return render_template("faq.html", categories=CATEGORIES)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message or len(name) > 120 or len(email) > 254 or len(message) > 5000:
        return redirect(url_for("home") + "?contact=error#contact")

    if not re.fullmatch(r"[^@\\s]+@[^@\\s]+\\.[^@\\s]+", email):
        return redirect(url_for("home") + "?contact=error#contact")

    api_key = os.getenv("RESEND_API_KEY")
    from_email = os.getenv("CONTACT_FROM_EMAIL")
    if not api_key or not from_email:
        app.logger.error("Contact mail is not configured: RESEND_API_KEY and CONTACT_FROM_EMAIL are required.")
        return redirect(url_for("home") + "?contact=error#contact")

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
                return redirect(url_for("home") + "?contact=sent#contact")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        app.logger.error("Contact mail failed: %s", exc)

    return redirect(url_for("home") + "?contact=error#contact")

@app.route("/over-trendmix")
def over_trendmix():
    return render_info_page("over-trendmix")


@app.route("/affiliate")
def affiliate():
    return render_info_page("affiliate")


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
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{slug}" for slug in CATEGORIES] + [f"{SITE_URL}/{path}" for path in INFO_PAGES]
    urls.append(f"{SITE_URL}/faq")
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" + "".join(f"<url><loc>{url}</loc></url>" for url in urls) + "</urlset>"
    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
