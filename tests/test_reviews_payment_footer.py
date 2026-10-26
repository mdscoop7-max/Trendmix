from app import app


def test_product_page_has_review_area_without_fake_stars():
    response = app.test_client().get("/beauty-care/elektrische-gezichtsroller")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'id="tm-reviews-title"' in html
    assert "TEST / DEMO — NIET ECHT" in html
    assert "Fictieve tekst voor de testweergave" in html
    assert '"aggregateRating"' not in html


def test_footer_displays_only_planned_payment_methods():
    for path in ("/", "/shop", "/beauty-care/elektrische-gezichtsroller"):
        response = app.test_client().get(path)
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Betaalmethoden in voorbereiding" in html
        assert "Betalen is op dit moment nog niet actief" in html
        assert 'role="img"' in html
        for payment in ("iDEAL / Wero", "Google Pay", "PayPal"):
            assert payment in html
