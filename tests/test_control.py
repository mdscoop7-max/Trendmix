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


def test_homepage_has_hero_image_fallbacks():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"data-product-image" in response.data


def test_sitemap_is_valid_xml_shape_and_has_products():
    client = app.test_client()
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert b"<urlset" in response.data
    assert b"/pc-componenten/" in response.data


def test_no_obsolete_affiliate_faq_copy_on_faq_page():
    client = app.test_client()
    response = client.get("/faq")
    assert response.status_code == 200
    assert b"externe aanbieder" not in response.data.lower()
    assert b"affiliate links" not in response.data.lower()


def test_language_bundle_has_no_obsolete_affiliate_store_model():
    from pathlib import Path
    content = Path("static/languages.js").read_text(encoding="utf-8").lower()
    for obsolete in ("independent product catalog", "onafhankelijke productcatalogus", "external retailer", "externe aanbieder"):
        assert obsolete not in content


def test_language_bundle_keeps_all_six_languages():
    from pathlib import Path
    content = Path("static/languages.js").read_text(encoding="utf-8")
    for language in ("nl:", "en:", "de:", "fr:", "it:", "es:"):
        assert language in content


def test_homepage_seo_and_search_action_metadata():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b'"SearchAction"' in response.data
    assert b'property="og:url"' in response.data
    assert b'name="twitter:card"' in response.data


def test_category_pages_have_resilient_images_and_social_metadata():
    client = app.test_client()
    for slug in ("pc-componenten", "gadgets", "smart-home", "beauty-care", "lifestyle-sport"):
        response = client.get(f"/{slug}")
        assert response.status_code == 200
        assert b"data-product-image" in response.data
        assert b'property="og:url"' in response.data


def test_product_page_uses_light_theme_and_structured_data():
    client = app.test_client()
    product = load_all_products()[0]
    response = client.get(product["product_url"])
    assert response.status_code == 200
    assert b'<meta name="theme-color" content="#f6f7fb">' in response.data
    assert b'"Product"' in response.data
    assert b'"BreadcrumbList"' in response.data


def test_search_matches_description_content():
    client = app.test_client()
    product = load_all_products()[0]
    words = [w.strip(".,:;()").lower() for w in str(product.get("description") or "").split() if len(w.strip(".,:;()")) > 5]
    assert words
    response = client.get("/?q=" + words[0])
    assert response.status_code == 200
    assert product["name"].encode() in response.data


def test_mobile_navigation_contains_core_shopping_tasks():
    client = app.test_client()
    response = client.get("/")
    for target in (b'/#collecties', b'/#featured', b'/winkelwagen', b'/contact'):
        assert target in response.data
