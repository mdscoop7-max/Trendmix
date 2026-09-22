from flask import Flask

app = Flask(__name__)

# Zorg ervoor dat deze variabelen elders in je script zijn gedefinieerd:
# EXPECTED_CATEGORIES = {...}
# ALLOWED_NETWORKS = [...]
# ALLOWED_MARGINS = [...]
# get_db() -> functie om databaseverbinding op te halen


def validate_database_products():
    """
    Controleert de producten en categorieën die daadwerkelijk
    in de SQLite-database staan.
    """
    db = get_db()

    try:
        errors = []

        # ====================================================
        # 1. DATABASESTRUCTUUR
        # ====================================================

        required_tables = {"categories", "products"}

        existing_tables = {
            row["name"]
            for row in db.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type = 'table'
            """).fetchall()
        }

        missing_tables = required_tables - existing_tables

        if missing_tables:
            for table in sorted(missing_tables):
                errors.append(
                    f"Database-tabel ontbreekt: '{table}'."
                )

        if errors:
            raise ValueError(
                "Databasevalidatie kan niet worden uitgevoerd: "
                "vereiste tabellen ontbreken."
            )

        # ====================================================
        # 2. CATEGORIEËN
        # ====================================================

        category_count = db.execute("""
            SELECT COUNT(*)
            FROM categories
        """).fetchone()[0]

        expected_category_count = len(EXPECTED_CATEGORIES)

        if category_count != expected_category_count:
            errors.append(
                f"Database moet {expected_category_count} categorieën "
                f"bevatten, maar bevat {category_count}."
            )

        category_rows = db.execute("""
            SELECT id, name
            FROM categories
            ORDER BY id
        """).fetchall()

        category_names = set()
        category_ids = set()

        for category in category_rows:
            category_id = category["id"]
            category_name = category["name"]

            # Categorie-ID
            if not isinstance(category_id, int):
                errors.append(
                    f"Categorie-ID '{category_id}' "
                    f"moet een integer zijn."
                )
            elif category_id in category_ids:
                errors.append(
                    f"Categorie-ID {category_id} "
                    f"komt meerdere keren voor."
                )
            else:
                category_ids.add(category_id)

            # Categorienaam
            if not isinstance(category_name, str):
                errors.append(
                    f"Categorie {category_id}: "
                    f"naam moet tekst zijn."
                )
                continue

            category_name = category_name.strip()

            if not category_name:
                errors.append(
                    f"Categorie {category_id}: "
                    f"naam mag niet leeg zijn."
                )
                continue

            if category_name in category_names:
                errors.append(
                    f"Categorie '{category_name}' "
                    f"komt meerdere keren voor."
                )

            category_names.add(category_name)

        # Verwachte categorieën
        for category_name in EXPECTED_CATEGORIES:
            if category_name not in category_names:
                errors.append(
                    f"Verwachte categorie ontbreekt: "
                    f"'{category_name}'."
                )

        # Onverwachte categorieën
        for category_name in category_names:
            if category_name not in EXPECTED_CATEGORIES:
                errors.append(
                    f"Onbekende categorie in database: "
                    f"'{category_name}'."
                )

        # ====================================================
        # 3. PRODUCTEN
        # ====================================================

        product_count = db.execute("""
            SELECT COUNT(*)
            FROM products
        """).fetchone()[0]

        expected_product_count = sum(
            EXPECTED_CATEGORIES.values()
        )

        if product_count != expected_product_count:
            errors.append(
                f"Database moet {expected_product_count} producten "
                f"bevatten, maar bevat {product_count}."
            )

        rows = db.execute("""
            SELECT
                p.*,
                c.name AS category
            FROM products p
            LEFT JOIN categories c
                ON c.id = p.category_id
            ORDER BY p.id
        """).fetchall()

        # ====================================================
        # 4. PRODUCT-ID'S
        # ====================================================

        ids = []

        for product in rows:
            product_id = product["id"]

            if not isinstance(product_id, int):
                errors.append(
                    f"Product-ID '{product_id}' "
                    f"moet een integer zijn."
                )
            else:
                ids.append(product_id)

        duplicates = sorted(
            {
                product_id
                for product_id in ids
                if ids.count(product_id) > 1
            }
        )

        if duplicates:
            errors.append(
                f"Product-ID's zijn niet uniek: {duplicates}"
            )

        # Controleer 1 t/m totaal aantal producten
        if product_count == expected_product_count:
            expected_ids = set(
                range(1, expected_product_count + 1)
            )
            actual_ids = set(ids)

            missing_ids = sorted(
                expected_ids - actual_ids
            )
            extra_ids = sorted(
                actual_ids - expected_ids
            )

            if missing_ids:
                errors.append(
                    f"Ontbrekende product-ID's: {missing_ids}"
                )

            if extra_ids:
                errors.append(
                    f"Onverwachte product-ID's: {extra_ids}"
                )

        # ====================================================
        # 5. PRODUCTVELDEN
        # ====================================================

        required_fields = {
            "id",
            "name",
            "brand",
            "price",
            "old_price",
            "image",
            "category_id",
            "badge",
            "rating",
            "reviews",
            "description",
            "affiliate_url",
            "affiliate_network",
            "margin",
            "is_offer",
            "category",
        }

        for product in rows:
            product_id = product["id"]

            # Velden controleren
            missing_fields = [
                field
                for field in required_fields
                if field not in product.keys()
            ]

            if missing_fields:
                errors.append(
                    f"Product {product_id}: "
                    f"velden ontbreken: "
                    f"{', '.join(sorted(missing_fields))}"
                )
                continue

            # Naam
            name = product["name"]
            if not isinstance(name, str):
                errors.append(
                    f"Product {product_id}: "
                    f"name moet tekst zijn."
                )
            elif not name.strip():
                errors.append(
                    f"Product {product_id}: "
                    f"name mag niet leeg zijn."
                )

            # Merk
            brand = product["brand"]
            if not isinstance(brand, str):
                errors.append(
                    f"Product {product_id}: "
                    f"brand moet tekst zijn."
                )
            elif not brand.strip():
                errors.append(
                    f"Product {product_id}: "
                    f"brand mag niet leeg zijn."
                )

            # Prijs
            price = product["price"]
            if (
                not isinstance(price, (int, float))
                or isinstance(price, bool)
            ):
                errors.append(
                    f"Product {product_id}: "
                    f"price moet een getal zijn."
                )
            elif price < 0:
                errors.append(
                    f"Product {product_id}: "
                    f"price mag niet negatief zijn."
                )

            # Oude prijs
            old_price = product["old_price"]
            if old_price is not None:
                if (
                    not isinstance(old_price, (int, float))
                    or isinstance(old_price, bool)
                ):
                    errors.append(
                        f"Product {product_id}: "
                        f"old_price moet een getal zijn."
                    )
                elif old_price <= 0:
                    errors.append(
                        f"Product {product_id}: "
                        f"old_price moet groter dan 0 zijn."
                    )

            # Afbeelding
            image = product["image"]
            if not isinstance(image, str):
                errors.append(
                    f"Product {product_id}: "
                    f"image moet tekst zijn."
                )
            elif not image.strip():
                errors.append(
                    f"Product {product_id}: "
                    f"image mag niet leeg zijn."
                )
            elif not image.strip().startswith("products/"):
                errors.append(
                    f"Product {product_id}: "
                    f"image moet beginnen met 'products/'."
                )

            # Categorie
            category_id = product["category_id"]
            category = product["category"]

            if category_id is None:
                errors.append(
                    f"Product {product_id}: "
                    f"category_id ontbreekt."
                )

            if category is None:
                errors.append(
                    f"Product {product_id}: "
                    f"categorie bestaat niet."
                )
            elif category not in EXPECTED_CATEGORIES:
                errors.append(
                    f"Product {product_id}: "
                    f"onbekende categorie '{category}'."
                )

            # Badge
            badge = product["badge"]
            if not isinstance(badge, str):
                errors.append(
                    f"Product {product_id}: "
                    f"badge moet tekst zijn."
                )

            # Rating
            rating = product["rating"]
            if (
                not isinstance(rating, (int, float))
                or isinstance(rating, bool)
            ):
                errors.append(
                    f"Product {product_id}: "
                    f"rating moet een getal zijn."
                )
            elif not 0 <= rating <= 5:
                errors.append(
                    f"Product {product_id}: "
                    f"rating moet tussen 0 en 5 liggen."
                )

            # Reviews
            reviews = product["reviews"]
            if (
                not isinstance(reviews, int)
                or isinstance(reviews, bool)
            ):
                errors.append(
                    f"Product {product_id}: "
                    f"reviews moet een integer zijn."
                )
            elif reviews < 0:
                errors.append(
                    f"Product {product_id}: "
                    f"reviews mag niet negatief zijn."
                )

            # Beschrijving
            description = product["description"]
            if not isinstance(description, str):
                errors.append(
                    f"Product {product_id}: "
                    f"description moet tekst zijn."
                )
            elif not description.strip():
                errors.append(
                    f"Product {product_id}: "
                    f"description mag niet leeg zijn."
                )

            # Affiliate URL
            affiliate_url = product["affiliate_url"]
            if not isinstance(affiliate_url, str):
                errors.append(
                    f"Product {product_id}: "
                    f"affiliate_url moet tekst zijn."
                )
            elif not affiliate_url.strip():
                errors.append(
                    f"Product {product_id}: "
                    f"affiliate_url mag niet leeg zijn."
                )
            else:
                normalized_url = affiliate_url.strip().lower()
                if not (
                    normalized_url.startswith("http://")
                    or normalized_url.startswith("https://")
                ):
                    errors.append(
                        f"Product {product_id}: "
                        f"affiliate_url moet beginnen met "
                        f"http:// of https://."
                    )

            # Affiliate netwerk
            affiliate_network = product["affiliate_network"]
            if affiliate_network not in ALLOWED_NETWORKS:
                errors.append(
                    f"Product {product_id}: "
                    f"ongeldig affiliate netwerk "
                    f"'{affiliate_network}'."
                )

            # Marge
            margin = product["margin"]
            if margin not in ALLOWED_MARGINS:
                errors.append(
                    f"Product {product_id}: "
                    f"ongeldige marge '{margin}'."
                )

            # Is offer
            is_offer = product["is_offer"]
            if is_offer not in (0, 1):
                errors.append(
                    f"Product {product_id}: "
                    f"is_offer moet 0 of 1 zijn."
                )

            # Aanbieding logica
            if is_offer == 1:
                if old_price is None:
                    errors.append(
                        f"Product {product_id}: "
                        f"aanbieding heeft geen old_price."
                    )
                elif (
                    isinstance(price, (int, float))
                    and not isinstance(price, bool)
                    and isinstance(old_price, (int, float))
                    and not isinstance(old_price, bool)
                    and old_price <= price
                ):
                    errors.append(
                        f"Product {product_id}: "
                        f"old_price ({old_price}) moet hoger "
                        f"zijn dan price ({price})."
                    )
            elif is_offer == 0 and old_price is not None:
                errors.append(
                    f"Product {product_id}: "
                    f"geen aanbieding, maar old_price "
                    f"is ingevuld."
                )

        # ====================================================
        # 6. CATEGORIE-AANTALLEN
        # ====================================================

        for category_name, expected_count in EXPECTED_CATEGORIES.items():
            actual_count = db.execute(
                """
                SELECT COUNT(*)
                FROM products p
                INNER JOIN categories c
                    ON c.id = p.category_id
                WHERE c.name = ?
                """,
                (category_name,)
            ).fetchone()[0]

            if actual_count != expected_count:
                errors.append(
                    f"Categorie '{category_name}': "
                    f"verwacht {expected_count}, "
                    f"gevonden {actual_count}."
                )

        # ====================================================
        # 7. PRODUCTEN ZONDER CATEGORIE
        # ====================================================

        products_without_category = db.execute("""
            SELECT p.id
            FROM products p
            LEFT JOIN categories c
                ON c.id = p.category_id
            WHERE c.id IS NULL
        """).fetchall()

        for row in products_without_category:
            errors.append(
                f"Product {row['id']}: "
                f"heeft geen geldige categorie."
            )

        # ====================================================
        # 8. SQLITE INTEGRITY
        # ====================================================

        integrity_result = db.execute(
            "PRAGMA integrity_check"
        ).fetchone()[0]

        if integrity_result != "ok":
            errors.append(
                f"SQLite integrity_check mislukt: "
                f"{integrity_result}"
            )

        # ====================================================
        # 9. FOREIGN KEYS
        # ====================================================

        foreign_key_errors = db.execute(
            "PRAGMA foreign_key_check"
        ).fetchall()

        for row in foreign_key_errors:
            errors.append(
                f"Foreign-key fout: {tuple(row)}"
            )

        # ====================================================
        # 10. RESULTAAT
        # ====================================================

        if errors:
            print()
            print("============================================")
            print("DATABASEVALIDATIE MISLUKT")
            print("============================================")
            print(f"Aantal fouten: {len(errors)}")
            print()

            for number, error in enumerate(errors, start=1):
                print(f"{number}. {error}")

            print("============================================")
            print()

            raise ValueError(
                f"Databasevalidatie mislukt met "
                f"{len(errors)} fout(en)."
            )

        # ====================================================
        # SUCCES
        # ====================================================

        print()
        print("============================================")
        print("TRENDMIX DATABASEVALIDATIE GESLAAGD")
        print("============================================")
        print(f"Categorieën : {category_count}")
        print(f"Producten   : {product_count}")
        print("--------------------------------------------")

        for category_name in EXPECTED_CATEGORIES:
            actual_count = db.execute(
                """
                SELECT COUNT(*)
                FROM products p
                INNER JOIN categories c
                    ON c.id = p.category_id
                WHERE c.name = ?
                """,
                (category_name,)
            ).fetchone()[0]

            print(
                f"{category_name:<20}: {actual_count}"
            )

        print("--------------------------------------------")
        print("SQLite integrity : OK")
        print("Foreign keys     : OK")
        print("Productvalidatie : OK")
        print("============================================")
        print()

        return True

    finally:
        db.close()


# ============================================================
# START FLASK-APPLICATIE
# ============================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )