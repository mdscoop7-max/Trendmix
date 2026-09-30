from app import CATEGORY_DIRS, app, load_all_products


def test_control_page_exists():
    client = app.test_client()
    response = client.get("/control")

    assert response.status_code == 200
    assert b"TrendMix Control" in response.data or b"Controle" in response.data


def test_shop_categories_have_20_products_with_images():
    products = load_all_products()
    category_counts = {}

    for product in products:
        category_counts[product.get("category")] = category_counts.get(product.get("category"), 0) + 1

    assert len(category_counts) >= 5

    for category_name, folder_name in CATEGORY_DIRS.items():
        matches = [p for p in products if p.get("category") == category_name]
        assert len(matches) >= 20, f"{category_name} heeft te weinig producten: {len(matches)}"
        assert all(p.get("image") or p.get("image_url") for p in matches), f"{category_name} mist afbeeldingen"


def test_all_main_category_pages_render():
    client = app.test_client()
    for category_slug in ("pc-componenten", "gadgets", "smart-home", "beauty-care", "lifestyle-sport"):
        response = client.get(f"/{category_slug}")
        assert response.status_code == 200, f"{category_slug} returned {response.status_code}"


def test_core_customer_pages_render():
    client = app.test_client()
    for path in ("/", "/faq", "/contact", "/over-trendmix", "/bestellen", "/retouren", "/voorwaarden", "/privacy", "/cookies", "/robots.txt", "/sitemap.xml"):
        response = client.get(path)
        assert response.status_code == 200, f"{path} returned {response.status_code}"


def test_cart_and_checkout_test_flow():
    client = app.test_client()
    product = load_all_products()[0]
    response = client.post("/winkelwagen", data={"action": "add", "product_id": product["id"]}, follow_redirects=True)
    assert response.status_code == 200
    assert product["name"].encode() in response.data
    response = client.get("/afrekenen")
    assert response.status_code == 200
    assert b"Testmodus" in response.data


def test_catalog_is_exactly_100_products():
    products = load_all_products()
    assert len(products) == 100
