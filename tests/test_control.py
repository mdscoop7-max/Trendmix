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
