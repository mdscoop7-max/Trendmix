"""Prevent mobile menu flashes: navigation styles must exist before body paint."""
from app import app

PAGES = ("/", "/gadgets", "/smart-home", "/beauty-care", "/lifestyle-sport",
         "/aanbiedingen", "/shop", "/contact", "/wishlist", "/winkelwagen")

def test_navigation_css_precedes_body_for_main_routes():
    client = app.test_client()
    for route in PAGES:
        resp = client.get(route)
        assert resp.status_code == 200, route
        html = resp.get_data(as_text=True)
        head = html.split("</head>", 1)[0]
        body = html.split("</head>", 1)[1]
        for css in ("trendmix-footer-unified.css", "trendmix-nav-early.css", "trendmix-ui-2026.css"):
            assert head.count(css) == 1, (route, css)
            assert css not in body, (route, css)
        assert head.index("trendmix-footer-unified.css") < head.index("trendmix-nav-early.css")
        assert head.index("trendmix-nav-early.css") < head.index("trendmix-ui-2026.css")
        assert 'id="tmMobileDrawer"' in body
        assert 'data-tm-menu-trigger' in body

def test_no_late_styles_or_removed_mobile_behaviour():
    from pathlib import Path
    partial = Path("templates/_bottomnav.html").read_text(encoding="utf-8")
    assert "<style>" not in partial
    assert partial.count("<script>") == 4
    css = Path("static/trendmix-nav-early.css").read_text(encoding="utf-8")
    assert ".tm-dock" in css
    assert ".tm-header-actions" in css
    assert ".tm-campaign" in css
