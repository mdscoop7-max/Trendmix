from app import app


def test_primary_navigation_highlights_only_current_category():
    client = app.test_client()
    categories = ("gadgets", "smart-home", "beauty-care", "home-living", "lifestyle-sport")
    for current in categories:
        response = client.get("/" + current)
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        for category in categories:
            expected = f'href="/{category}" class="nav-link'
            assert expected in html
            anchor = html.split(expected, 1)[1].split(">", 1)[0]
            assert ("is-active" in anchor) == (category == current), (current, category)
        assert html.count('is-active" aria-current="page"') >= 1


def test_homepage_does_not_preselect_gadgets():
    html = app.test_client().get("/").get_data(as_text=True)
    assert 'href="/gadgets" class="nav-link is-active"' not in html
    assert 'href="/gadgets" class="selected"' not in html
