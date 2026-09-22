import json
import re
import os
import urllib.request
import urllib.error
from pathlib import Path
from flask import Flask, Response, current_app, render_template, request, redirect, url_for, session

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

CATEGORY_DIRS = {meta["name"]: slug for slug, meta in CATEGORIES.items()}


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
            yield enrich_product(product, slug, index)


def featured_mix():
    mixed = []
    for index in range(4):
        for slug in CATEGORIES:
            items = products.get(slug, [])
            if index < len(items):
                mixed.append(enrich_product(items[index], slug, index))
            if len(mixed) >= 10:
                return mixed
    return mixed


def category_images():
    return {slug: (items[0].get("image", "") if items else "") for slug, items in products.items()}


def slugify(value):
    value = str(value or "").lower()
    value = value.replace("+", " plus ").replace("&", " en ")
    value = re.sub(r"[^a-z0-9\s-]", "", value).strip()
    return re.sub(r"[-\s]+", "-", value)


def product_url(product):
    category_slug = product["category_slug"]
    subcategory_slug = product.get("subcategory_slug") or slugify(product.get("subcategory") or category_slug)
    product_slug = product["slug"]
    try:
        return url_for(
            "product_detail",
            category_slug=category_slug,
            subcategory_slug=subcategory_slug,
            product_slug=product_slug,
        )
    except RuntimeError:
        return f"/{category_slug}/{subcategory_slug}/{product_slug}"


def enrich_product(product, category_slug, index):
    item = dict(product)
    item["category_slug"] = category_slug
    item["category_name"] = CATEGORIES[category_slug]["name"]
    item["index"] = index
    item.setdefault("id", f"tm-{category_slug}-{slugify(item.get('name'))}-{index}")
    item.setdefault("slug", slugify(item.get("name")) or f"product-{index + 1}")
    item.setdefault("subcategory", CATEGORIES[category_slug]["name"])
    item.setdefault("subcategory_slug", slugify(item["subcategory"]))
    item.setdefault("brand", None)
    item.setdefault("old_price", None)
    item.setdefault("badge", None)
    item.setdefault("stock_status", "unknown")
    item.setdefault("stock_quantity", None)
    item.setdefault("delivery_time", "Nog te bevestigen")
    item.setdefault("images", [item["image"]] if item.get("image") else [])
    item.setdefault("short_description", item.get("description") or f"{item['name']} binnen {item['category_name']}.")
    item.setdefault("description", item.get("short_description") or f"{item['name']} is onderdeel van de TrendMix-collectie.")
    item.setdefault("specifications", {})
    item.setdefault("usps", [])
    item.setdefault("seo_title", f"{item['name']} | TrendMix")
    item.setdefault("seo_description", f"{item['name']} binnen {item['category_name']}. Bekijk prijs, productinformatie en alternatieven bij TrendMix.")
    item.setdefault("faq", [])
    item.setdefault("related_product_ids", [])
    item["product_url"] = product_url(item)
    return item


def cart_items():
    return session.get("trendmix_cart", [])


def cart_count():
    return sum(max(1, int(item.get("qty", 1))) for item in cart_items())


def cart_total():
    return sum(
        float(item.get("price", 0) or 0) * max(1, int(item.get("qty", 1)))
        for item in cart_items()
    )


def load_all_products():
    all_products = []
    for category_slug, items in products.items():
        for index, raw in enumerate(items):
            item = enrich_product(raw, category_slug, index)
            item["category"] = item.get("category_name", category_slug)
            all_products.append(item)
    for index, product in enumerate(all_products, start=1):
        product["id"] = index
    return all_products


def find_product(product_id):
    product_id = str(product_id or "").strip()
    for category_slug, items in products.items():
        for index, raw in enumerate(items):
            item = enrich_product(raw, category_slug, index)
            if item["id"] == product_id:
                return item
    match = re.fullmatch(r"([a-z0-9-]+)-(\d+)", product_id)
    if match and match.group(1) in products:
        index = int(match.group(2))
        items = products[match.group(1)]
        if 0 <= index < len(items):
            return enrich_product(items[index], match.group(1), index)

    try:
        numeric_id = int(product_id)
    except ValueError:
        numeric_id = None
    if numeric_id is not None:
        for product in load_all_products():
            if product.get("id") == numeric_id:
                return product
    return None


def filter_products(product_list, category=None, search=None):
    result = list(product_list)
    if category:
        result = [p for p in result if p.get("category") == category or p.get("category_name") == category]
    if search:
        needle = str(search).strip().lower()
        if needle:
            result = [
                p for p in result
                if needle in str(p.get("name", "")).lower()
                or needle in str(p.get("brand", "")).lower()
                or needle in str(p.get("description", "")).lower()
            ]
    return result


# WooCommerce is optional during development. Keep secrets in Vercel environment variables.
def woo_configured():
    return bool(os.getenv("WOOCOMMERCE_URL") and os.getenv("WOOCOMMERCE_CONSUMER_KEY") and os.getenv("WOOCOMMERCE_CONSUMER_SECRET"))


def woo_request(method, path, payload=None):
    base = os.getenv("WOOCOMMERCE_URL", "").rstrip("/")
    key = os.getenv("WOOCOMMERCE_CONSUMER_KEY", "")
    secret = os.getenv("WOOCOMMERCE_CONSUMER_SECRET", "")
    if not base or not key or not secret:
        return None
    url = f"{base}/wp-json/wc/v3/{path.lstrip('/')}"
    body = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request_obj = urllib.request.Request(url, data=body, headers=headers, method=method.upper())
    import base64
    token = base64.b64encode(f"{key}:{secret}".encode("utf-8")).decode("ascii")
    request_obj.add_header("Authorization", f"Basic {token}")
    try:
        with urllib.request.urlopen(request_obj, timeout=12) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as exc:
        app.logger.error("WooCommerce API request failed: %s", exc)
        return None


def create_woo_order(cart, customer):
    line_items = []
    for item in cart:
        product = find_product(item.get("id"))
        woo_id = (product or {}).get("woocommerce_product_id")
        if not woo_id:
            return None, "Producten zijn nog niet aan WooCommerce gekoppeld."
        line_items.append({"product_id": int(woo_id), "quantity": max(1, int(item.get("qty", 1)))})
    payload = {
        "payment_method": "",
        "payment_method_title": "Nog te betalen",
        "set_paid": False,
        "billing": customer,
        "shipping": customer,
        "line_items": line_items,
    }
    result = woo_request("POST", "orders", payload)
    if not result or not result.get("id"):
        return None, "De WooCommerce-bestelling kon niet worden aangemaakt."
    return result, None


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


@app.route("/shop")
def shop():
    category = request.args.get("category")
    search = request.args.get("q", "").strip()
    all_products = load_all_products()
    if category and category not in CATEGORY_DIRS:
        category = None
    if category:
        category_name = category
        filtered = filter_products(all_products, category=category_name, search=search)
    else:
        filtered = filter_products(all_products, search=search)
    return render_template("shop.html", products=filtered, category=category, search=search, categories=CATEGORIES)


@app.route("/products")
def products_page():
    return redirect(url_for("shop"), code=302)


@app.route("/account")
def account():
    return render_template("account.html", categories=CATEGORIES)


@app.route("/wishlist")
def wishlist():
    return render_template("wishlist.html", categories=CATEGORIES, products=[])


@app.route("/cart")
def cart():
    return redirect(url_for("winkelwagen"), code=302)


@app.route("/product/<int:product_id>")
def product(product_id):
    product_item = find_product(product_id)
    if not product_item:
        return "Product niet gevonden", 404
    return redirect(product_item["product_url"], code=302)


@app.route("/control")
def control():
    all_products = load_all_products()
    category_counts = {}
    for product in all_products:
        category_name = product.get("category") or product.get("category_name") or "Onbekend"
        category_counts[category_name] = category_counts.get(category_name, 0) + 1

    offer_count = sum(1 for product in all_products if product.get("old_price") or product.get("is_offer"))
    avg_price = round(sum(float(product.get("price", 0) or 0) for product in all_products) / len(all_products), 2) if all_products else 0
    top_category = max(category_counts.items(), key=lambda item: item[1])[0] if category_counts else "N/A"
    featured_products = sorted(all_products, key=lambda p: (float(p.get("price", 0) or 0), p.get("name", "")), reverse=True)[:8]

    return render_template(
        "control.html",
        products=featured_products,
        stats={
            "total_products": len(all_products),
            "total_categories": len(category_counts),
            "offers": offer_count,
            "avg_price": avg_price,
            "top_category": top_category,
        },
        category_counts=sorted(category_counts.items()),
        categories=CATEGORIES,
    )


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
    category_products = [
        enrich_product(item, category_slug, index)
        for index, item in enumerate(products[category_slug])
    ]
    subcategories = {}
    for item in category_products:
        subcategories.setdefault(item["subcategory_slug"], {
            "name": item["subcategory"],
            "slug": item["subcategory_slug"],
            "count": 0,
        })
        subcategories[item["subcategory_slug"]]["count"] += 1
    return render_template(
        "category.html",
        category_name=category["name"],
        category_icon=category["icon"],
        category_eyebrow=category["eyebrow"],
        category_slug=category_slug,
        categories=CATEGORIES,
        products=category_products,
        subcategories=list(subcategories.values()),
    )


@app.route("/<category_slug>/<subcategory_slug>/")
def subcategory_page(category_slug, subcategory_slug):
    if category_slug not in products:
        return "Pagina niet gevonden", 404
    matching = []
    subcategory_name = None
    for index, raw in enumerate(products[category_slug]):
        item = enrich_product(raw, category_slug, index)
        if item["subcategory_slug"] == subcategory_slug:
            matching.append(item)
            subcategory_name = item["subcategory"]
    if not matching:
        return "Pagina niet gevonden", 404
    category = CATEGORIES[category_slug]
    return render_template(
        "category.html",
        category_name=category["name"],
        category_icon=category["icon"],
        category_eyebrow=category["eyebrow"],
        category_slug=category_slug,
        categories=CATEGORIES,
        products=matching,
        subcategories=[],
        subcategory_slug=subcategory_slug,
        subcategory_name=subcategory_name,
    )


@app.route("/product/<category_slug>/<int:product_index>")
def legacy_product_detail(category_slug, product_index):
    if category_slug not in products or product_index < 0 or product_index >= len(products[category_slug]):
        return "Product niet gevonden", 404
    product = enrich_product(products[category_slug][product_index], category_slug, product_index)
    return redirect(product["product_url"], code=301)


@app.route("/<category_slug>/<subcategory_slug>/<product_slug>")
def product_detail(category_slug, subcategory_slug, product_slug):
    if category_slug not in products:
        return "Product niet gevonden", 404
    match = None
    for index, raw in enumerate(products[category_slug]):
        item = enrich_product(raw, category_slug, index)
        if item["slug"] == product_slug and item["subcategory_slug"] == subcategory_slug:
            match = item
            break
    if not match:
        for index, raw in enumerate(products[category_slug]):
            item = enrich_product(raw, category_slug, index)
            if item["slug"] == product_slug:
                return redirect(item["product_url"], code=301)
        return "Product niet gevonden", 404
    related = []
    for index, raw in enumerate(products[category_slug]):
        item = enrich_product(raw, category_slug, index)
        if item["id"] != match["id"] and (
            item["subcategory_slug"] == match["subcategory_slug"] or not related
        ):
            related.append(item)
        if len(related) >= 6:
            break
    return render_template(
        "product.html",
        product=match,
        product_index=match["index"],
        category_slug=category_slug,
        category_name=CATEGORIES[category_slug]["name"],
        categories=CATEGORIES,
        related=related,
    )


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


@app.route("/afrekenen", methods=["GET", "POST"])
def afrekenen():
    cart = [dict(item) for item in cart_items()]
    if not cart:
        return redirect(url_for("winkelwagen"))
    total = sum(float(item.get("price", 0) or 0) * max(1, int(item.get("qty", 1))) for item in cart)
    order = None
    error = None
    if request.method == "POST":
        customer = {
            "first_name": request.form.get("first_name", "").strip(),
            "last_name": request.form.get("last_name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "address_1": request.form.get("address_1", "").strip(),
            "postcode": request.form.get("postcode", "").strip(),
            "city": request.form.get("city", "").strip(),
            "country": "NL",
        }
        if not all(customer.values()):
            error = "Vul alle verplichte gegevens in."
        elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", customer["email"]):
            error = "Vul een geldig e-mailadres in."
        elif woo_configured():
            order, error = create_woo_order(cart, customer)
            if order:
                session.pop("trendmix_cart", None)
                return render_template("checkout.html", categories=CATEGORIES, cart=[], cart_count=0, cart_total=0, test_mode=False, order=order, error=None)
        else:
            session["trendmix_test_checkout"] = customer
            return render_template("checkout.html", categories=CATEGORIES, cart=cart, cart_count=cart_count(), cart_total=total, test_mode=True, order=None, error=None)
    return render_template("checkout.html", categories=CATEGORIES, cart=cart, cart_count=cart_count(), cart_total=total, test_mode=False, order=order, error=error)


@app.route("/faq")
def faq():
    return render_template("faq.html", categories=CATEGORIES)

@app.route("/contact", methods=["GET"])
def contact_page():
    return render_template("contact.html", categories=CATEGORIES, search_query="")

@app.route("/contact", methods=["POST"])
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
        subcats = {}
        for index, raw in enumerate(items):
            item = enrich_product(raw, slug, index)
            subcats[item["subcategory_slug"]] = item
        for subcat_slug in subcats:
            urls.append(f"{SITE_URL}/{slug}/{subcat_slug}/")
        for index, raw in enumerate(items):
            urls.append(f"{SITE_URL}{enrich_product(raw, slug, index)['product_url']}")
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" + "".join(f"<url><loc>{url}</loc></url>" for url in urls) + "</urlset>"
    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
