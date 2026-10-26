from app import app


def test_account_page_is_honest_about_status():
    client = app.test_client()
    response = client.get("/account")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "Een veilige klantomgeving is in voorbereiding" in html
    assert "nog niet beschikbaar" in html
    assert 'href="/wishlist"' in html
    assert 'href="/winkelwagen"' in html
    assert 'href="/contact"' in html
    assert 'type="password"' not in html


def test_account_does_not_show_private_orders():
    html = app.test_client().get("/account").get_data(as_text=True)
    assert "Deze pagina toont momenteel geen persoonlijke ordergegevens" in html
