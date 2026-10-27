# Trend Mix — checklist voor de laptopcontrole

## Klaargezet op ontwikkelbranch
Branch: `seo/trendmix-content-audit-20261026`.
Niets is naar `main` gemerged of naar productie gedeployed. De bestaande homepagehero is niet aangepast.

## Laptop: ophalen
```powershell
cd C:\Users\user\Desktop\Trendmix-main
git status
git fetch origin
git switch seo/trendmix-content-audit-20261026
git pull --ff-only origin seo/trendmix-content-audit-20261026
python -m pytest -q
python app.py
```
Let op: inspecteer eventuele lokale onopgeslagen bestanden met `git status` voordat je schakelt. Gooi niets weg.

## Functionele en visuele QA
1. Desktop (1440px), tablet (768px), mobiel (390px, 375px en 320px): productrasters, zoekbalk, filters, navigatie, productfoto's/zoom, footer, NL/EN; geen horizontale scroll.
2. Homepagehero vergelijken met vorige versie: tekst, animatie, afbeeldingen en afmetingen moeten ongewijzigd zijn.
3. `/faq`, `/contact`, `/bestellen`, `/retouren`, `/privacy`, `/cookies`, `/voorwaarden`, `/over-trendmix`: correcte teksten, links en mobiele leesbaarheid.
4. Test contactformulier zonder RESEND-config: toont duidelijk dat verzenden niet beschikbaar is; mag nooit succes veinzen.
5. Productpagina: demo-review is standaard verborgen; alleen zichtbaar met lokale `TRENDMIX_SHOW_DEMO_REVIEWS=1`, nooit op Vercel. Echte reviews nog niet actief.
6. Winkelwagen: plus/min, verwijderen, lege winkelwagen, aantallen maximaal 99 en actuele productprijzen; productsubtotaal klopt.
7. `/afrekenen`: vermeldt duidelijk testfase; verzendkosten zijn nog onbekend; gebruik fictieve klantgegevens. Geen echte betaling/order bevestigen.
8. SEO: juiste titel, meta description, canonical, JSON-LD en sitemap. Demo-producten zijn `noindex` en staan niet in sitemap.
9. `/beheer`: standaard 404; bij geldige testcredentials alleen-lezen, nooit publiek openzetten.
10. Test veiligheidsheaders, CSRF op formulieren en GitHub Actions-status.

## Voor commerciële livegang — nog niet voltooid
- EU-dropshippingleveranciers contractueel vastleggen; authentieke feed en afbeeldingsrechten, actuele prijs/voorraad/levering.
- Werkende betaalprovider, betaalbevestiging, bestelverwerking, retourafhandeling en controle op verzendkosten.
- Werkend beheerdashboard met beveiligde persistente productmutaties en auditlog.
- Echt reviewproces: alleen reviews van gekoppelde, geverifieerde aankopen publiceren; geen demodata of nepsterren.
- Contact-e-mail koppelen en testen. Wettelijke bedrijfsgegevens en toepasselijke consumenteninformatie invullen en juridisch controleren.
- Visuele laptopcontrole vóór een merge of publicatie; geen automatische publicatie.
