from flask import Flask, render_template, request

app = Flask(__name__)


# =========================================================
# PRODUCTEN
# =========================================================

products = {

    "pc-componenten": [
        {"name": "Gaming Keyboard", "price": 49.95, "icon": "⌨️", "image": ""},
        {"name": "Gaming Mouse", "price": 29.95, "icon": "🖱️", "image": ""},
        {"name": "USB-C Hub", "price": 34.95, "icon": "🔌", "image": ""},
        {"name": "Laptop Stand", "price": 39.95, "icon": "💻", "image": ""},
        {"name": "RGB Mouse Pad", "price": 24.95, "icon": "🖥️", "image": ""},
        {"name": "Wireless Keyboard", "price": 44.95, "icon": "⌨️", "image": ""},
        {"name": "Webcam Full HD", "price": 54.95, "icon": "📷", "image": ""},
        {"name": "USB Microphone", "price": 59.95, "icon": "🎙️", "image": ""},
    ],


    "gadgets": [
        {"name": "Wireless Earbuds Case", "price": 29.95, "icon": "🎧", "image": ""},
        {"name": "Portable Bluetooth Speaker", "price": 39.95, "icon": "🔊", "image": ""},
        {"name": "Mini Power Bank", "price": 29.95, "icon": "🔋", "image": ""},
        {"name": "Universal Phone Mount", "price": 24.95, "icon": "📱", "image": ""},
        {"name": "Foldable Phone Holder", "price": 19.95, "icon": "📱", "image": ""},
        {"name": "USB-C Fast Charging Cable", "price": 14.95, "icon": "🔌", "image": ""},
        {"name": "Wireless Charging Pad", "price": 29.95, "icon": "⚡", "image": ""},
        {"name": "Portable Fan", "price": 24.95, "icon": "🌀", "image": ""},
    ],


    "smart-home": [
        {"name": "Smart LED Strip", "price": 29.95, "icon": "💡", "image": ""},
        {"name": "Smart LED Bulb", "price": 19.95, "icon": "💡", "image": ""},
        {"name": "Smart Plug", "price": 24.95, "icon": "🔌", "image": ""},
        {"name": "Motion Sensor", "price": 29.95, "icon": "📡", "image": ""},
        {"name": "Smart Night Light", "price": 22.95, "icon": "🌙", "image": ""},
        {"name": "Mini Security Camera", "price": 49.95, "icon": "📷", "image": ""},
        {"name": "Digital Alarm Clock", "price": 34.95, "icon": "⏰", "image": ""},
        {"name": "Smart Temperature Sensor", "price": 27.95, "icon": "🌡️", "image": ""},
    ],


    "beauty-care": [
        {"name": "Mini Facial Cleaner", "price": 29.95, "icon": "✨", "image": ""},
        {"name": "Beauty Mirror", "price": 39.95, "icon": "🪞", "image": ""},
        {"name": "Makeup Organizer", "price": 24.95, "icon": "💄", "image": ""},
        {"name": "Face Massage Roller", "price": 19.95, "icon": "✨", "image": ""},
        {"name": "Travel Beauty Bag", "price": 24.95, "icon": "👜", "image": ""},
        {"name": "Hair Styling Brush", "price": 34.95, "icon": "💇", "image": ""},
        {"name": "Cosmetic Storage Box", "price": 29.95, "icon": "💄", "image": ""},
        {"name": "Makeup Brush Set", "price": 27.95, "icon": "🖌️", "image": ""},
    ],


    "lifestyle-sport": [
        {"name": "Sports Water Bottle", "price": 24.95, "icon": "🥤", "image": ""},
        {"name": "Fitness Resistance Bands", "price": 29.95, "icon": "🏋️", "image": ""},
        {"name": "Yoga Mat", "price": 34.95, "icon": "🧘", "image": ""},
        {"name": "Running Waist Bag", "price": 22.95, "icon": "🏃", "image": ""},
        {"name": "Fitness Phone Holder", "price": 19.95, "icon": "📱", "image": ""},
        {"name": "Gym Towel", "price": 14.95, "icon": "🏋️", "image": ""},
        {"name": "Sports Backpack", "price": 44.95, "icon": "🎒", "image": ""},
        {"name": "Portable Water Bottle", "price": 21.95, "icon": "🥤", "image": ""},
    ],


    "aanbiedingen": [
        {"name": "USB-C Fast Charging Cable", "price": 29.95, "icon": "🔌", "image": ""},
        {"name": "Wireless Earbuds Case", "price": 29.95, "icon": "🎧", "image": ""},
        {"name": "LED Desk Lamp", "price": 29.95, "icon": "💡", "image": ""},
        {"name": "Phone Stand", "price": 29.95, "icon": "📱", "image": ""},
        {"name": "Cable Organizer Set", "price": 29.95, "icon": "🔌", "image": ""},
        {"name": "Portable Bluetooth Speaker", "price": 29.95, "icon": "🔊", "image": ""},
        {"name": "Laptop Stand", "price": 29.95, "icon": "💻", "image": ""},
        {"name": "Wireless Charging Pad", "price": 29.95, "icon": "⚡", "image": ""},
        {"name": "Mini Cleaning Brush", "price": 29.95, "icon": "🧹", "image": ""},
        {"name": "Travel Organizer", "price": 29.95, "icon": "🧳", "image": ""},
        {"name": "USB Hub", "price": 29.95, "icon": "🔌", "image": ""},
        {"name": "Desk Organizer", "price": 29.95, "icon": "🗂️", "image": ""},
        {"name": "Smart LED Strip", "price": 29.95, "icon": "💡", "image": ""},
        {"name": "Foldable Phone Holder", "price": 29.95, "icon": "📱", "image": ""},
        {"name": "Keyboard Cleaning Kit", "price": 29.95, "icon": "⌨️", "image": ""},
        {"name": "Portable Fan", "price": 29.95, "icon": "🌀", "image": ""},
        {"name": "Screen Cleaning Kit", "price": 29.95, "icon": "🧽", "image": ""},
        {"name": "Mini Power Bank", "price": 29.95, "icon": "🔋", "image": ""},
        {"name": "Cable Storage Bag", "price": 29.95, "icon": "🎒", "image": ""},
        {"name": "Universal Phone Mount", "price": 29.95, "icon": "📱", "image": ""},
    ]

}


# =========================================================
# CATEGORIE-INFORMATIE
# =========================================================

categories = {

    "pc-componenten": {
        "name": "PC-Componenten",
        "icon": "🖥️"
    },

    "gadgets": {
        "name": "Gadgets",
        "icon": "🔌"
    },

    "smart-home": {
        "name": "Smart Home",
        "icon": "🏠"
    },

    "beauty-care": {
        "name": "Beauty & Care",
        "icon": "💄"
    },

    "lifestyle-sport": {
        "name": "Lifestyle & Sport",
        "icon": "🏃"
    },

    "aanbiedingen": {
        "name": "Aanbiedingen",
        "icon": "🔥"
    }

}


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    popular_products = []

    for category_products in products.values():
        popular_products.extend(category_products[:2])

    offers = products["aanbiedingen"][:8]

    return render_template(
        "index.html",
        popular_products=popular_products,
        offers=offers
    )


# =========================================================
# ALLE CATEGORIEPAGINA'S
# =========================================================

@app.route("/<category_slug>")
def category_page(category_slug):

    if category_slug not in categories:
        return "Pagina niet gevonden", 404

    category = categories[category_slug]

    return render_template(
        "category.html",

        category_name=category["name"],

        category_icon=category["icon"],

        products=products[category_slug]
    )


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )