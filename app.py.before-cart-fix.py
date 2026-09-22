import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Uitgebreide productdatabase gebaseerd op het professionele ontwerp
PRODUCTS_DB = [
    {
        "id": 1,
        "name": "BeeGlow Verfijnde LED-lamp",
        "category": "Gadgets",
        "badge": "Bestseller",
        "price": 29.95,
        "rating": 4.8,
        "reviews": 128,
        "desc": "Stijlvolle en energiezuinige LED-lamp voor sfeervolle verlichting in huis.",
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 2,
        "name": "HeatMate Draagbare Handwarmer",
        "category": "Gadgets",
        "badge": "Hot",
        "price": 24.95,
        "rating": 4.9,
        "reviews": 96,
        "desc": "Compacte, oplaadbare handwarmer met instelbare warmtestanden.",
        "image": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 3,
        "name": "PurrChase Interactief Kattenspeelgoed",
        "category": "Lifestyle & Sport",
        "badge": "Trend",
        "price": 19.95,
        "rating": 4.7,
        "reviews": 74,
        "desc": "Houd je kat urenlang actief en nieuwsgierig met automatische beweging.",
        "image": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 4,
        "name": "GlowGroom Huisdierborstel",
        "category": "Beauty & Care",
        "badge": "Top Pick",
        "price": 34.95,
        "rating": 4.8,
        "reviews": 54,
        "desc": "Ergonomische verzorgingsborstel voor een glanzende en klitvrije vacht.",
        "image": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 5,
        "name": "MapQuest Waterdichte Wereldkaart",
        "category": "Lifestyle & Sport",
        "badge": "Bestseller",
        "price": 19.95,
        "rating": 4.9,
        "reviews": 112,
        "desc": "Kras- en waterbestendige wereldkaart voor reizigers en ontdekkingsreizigers.",
        "image": "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 6,
        "name": "FairyNest Hangende Vogelhuisje",
        "category": "Smart Home",
        "badge": "Nieuw",
        "price": 24.95,
        "rating": 4.6,
        "reviews": 68,
        "desc": "Natuurlijk en sfeervol vogelhuisje voor in elke achtertuin of balkon.",
        "image": "https://images.unsplash.com/photo-1444464666168-49d633b86797?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 7,
        "name": "USB-C Hub Pro",
        "category": "PC Componenten",
        "badge": "Bestseller",
        "price": 47.95,
        "rating": 4.8,
        "reviews": 124,
        "desc": "Snelle USB-C adapter met 4K HDMI en Power Delivery.",
        "image": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=400&auto=format&fit=crop&q=80"
    },
    {
        "id": 8,
        "name": "Smart RGB Lamp",
        "category": "Smart Home",
        "badge": "Populair",
        "price": 21.95,
        "rating": 4.6,
        "reviews": 89,
        "desc": "Bedien deze sfeervolle lamp eenvoudig via je smartphone of stem.",
        "image": "https://images.unsplash.com/photo-1550985616-11b15456f728?w=400&auto=format&fit=crop&q=80"
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS_DB, cart_count=2, wishlist_count=0)

@app.route('/shop')
def shop():
    category = request.args.get('category')
    search_query = request.args.get('q', '').lower()
    
    filtered_products = PRODUCTS_DB
    if category:
        filtered_products = [p for p in filtered_products if p['category'].lower() == category.lower()]
    if search_query:
        filtered_products = [p for p in filtered_products if search_query in p['name'].lower() or search_query in p['desc'].lower()]
        
    return render_template('shop.html', products=filtered_products, search=search_query, cart_count=2, wishlist_count=0)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS_DB if p['id'] == product_id), PRODUCTS_DB[0])
    return render_template('product.html', product=product, cart_count=2, wishlist_count=0)

@app.route('/cart')
def cart():
    return render_template('cart.html', cart_count=2, wishlist_count=0)

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html', products=[], cart_count=2, wishlist_count=0)

@app.route('/account')
def account():
    return render_template('account.html', cart_count=2, wishlist_count=0)

@app.route('/checkout')
def checkout():
    items = [{"name": "BeeGlow Verfijnde LED-lamp", "price": 29.95, "quantity": 1, "subtotal": 29.95}]
    return render_template('checkout.html', items=items, total=29.95, shipping=0.0, grand_total=29.95, cart_count=2, wishlist_count=0)

if __name__ == '__main__':
    app.run(debug=True)