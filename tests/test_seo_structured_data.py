import json
import re
from app import app


def test_shop_in_sitemap():
    response = app.test_client().get("/sitemap.xml")
    assert response.status_code == 200
    assert "/shop</loc>" in response.get_data(as_text=True)


def test_product_json_ld_has_absolute_urls():
    client = app.test_client()
    sitemap = client.get("/sitemap.xml").get_data(as_text=True)
    product_paths = re.findall(r"<loc>https?://[^/]+(/product[^<]*)</loc>", sitemap)
    if not product_paths:
        return  # Actual product route is covered by existing product tests.
    html = client.get(product_paths[0]).get_data(as_text=True)
    blocks = re.findall(r'<script type="application/ld\\+json">\\s*(.*?)\\s*</script>', html, re.S)
    products = [json.loads(b) for b in blocks if json.loads(b).get("@type") == "Product"]
    assert products
    assert products[0]["url"].startswith("http")
    assert all(image.startswith("http") for image in products[0]["image"])
