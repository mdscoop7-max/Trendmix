/* TrendMix language extension: adds German as the sixth supported language. */
translations.de={
  topline:'Neue Kollektion · 5 klare Kategorien · mobil bereit',discover:'Entdecken',search:'TrendMix durchsuchen...',heroEyebrow:'TrendMix · Produktentdeckung',heroTitle:'Besser entdecken.<br><em>Smarter auswählen.</em>',heroText:'Von leistungsstarken PC-Komponenten über Gadgets und Smart Home bis Beauty und Sport. Fünf klare Kollektionen, übersichtlich präsentiert und leicht zu vergleichen.',viewCollections:'Kollektionen ansehen →',viewFeatured:'Highlights ansehen',categories:'Kategorien',products:'Produkte',languages:'Sprachen',collections:'Kollektionen',access:'Zugang',searchEyebrow:'Suche',searchTitle:'Suchergebnisse',noResults:'Keine Ergebnisse',noResultsText:'Versuche einen anderen Suchbegriff.',collectionsEyebrow:'Smarter shoppen',collectionsTitle:'Wähle deine Kollektion',collectionsText:'Fünf klare Kollektionen, schnell und übersichtlich.',featuredEyebrow:'Ausgewählte Produkte',featuredTitle:'Etwas Besonderes aus jeder Kollektion',allCollections:'Alle Kollektionen →',methodEyebrow:'Unser Ansatz',methodTitle:'Kein endloser Katalog.<br>Eine klare Auswahl.',methodText:'TrendMix ist bewusst einfacher als große Marktplätze: weniger Kategorien, bessere Orientierung und eine ruhige Präsentation.',step1Title:'Auswählen',step1Text:'Relevanz und passende Kategorie.',step2Title:'Präsentieren',step2Text:'Starke Bilder und kurze Informationen.',step3Title:'Entdecken',step3Text:'Schnell vom Produkt zur Kollektion.',valueTitle:'Weniger suchen.<br>Mehr entdecken.',valueText:'Ein moderner Produktkatalog ohne gefälschte Bewertungen, übertriebene Versprechen oder unnötige Bildschirme.',value1:'Klare Kategorien',value2:'Starke Produktbilder',value3:'Mobile first',value4:'Keine doppelten Inhalte',footerText:'Ein unabhängiger Produktkatalog für moderne Trends, Technik, Home, Beauty und Lifestyle.',footerCollections:'Kollektionen',footerExplore:'Entdecken',footerCategories:'Kategorien',footerHighlights:'Highlights',footerHome:'Startseite',footerInfo:'TrendMix',footerNote:'Unabhängiger Produktkatalog.<br>Keine erfundenen Bewertungen oder Versprechen.',footerBottom:'Modern · übersichtlich · zugänglich',categoryIntro:'Eine klare Auswahl von Produkten, ruhig präsentiert und einfach auf Desktop und Mobilgerät anzusehen.',allProducts:'Alle Produkte',uniqueItems:'einzigartige Artikel',sortBy:'Sortieren',moreToDiscover:'Mehr zu entdecken.',moreText:'Wähle eine andere Kollektion und entdecke den restlichen Katalog.',curatedBadge:'TrendMix Auswahl',viewProduct:'→',backToCollection:'← Zurück zur Kollektion',backToCollectionBtn:'Kollektion ansehen →',otherCategory:'Andere Kategorie',priceNote:'Richtpreis aus dem Katalog · prüfe den aktuellen Preis und die Verfügbarkeit beim Anbieter.',productDescription:'Ein ausgewähltes TrendMix-Produkt aus dieser Kollektion. Nutze die Kollektion, um Alternativen zu entdecken und Produkte zu vergleichen.',point1:'Klare Auswahl',point2:'Starke Produktbilder',point3:'Mobilfreundlich',relatedTitle:'Mehr aus dieser Kollektion',noProducts:'Keine Produkte'
};

/* Contact form translations */
const sortTranslations={
 nl:{sortRecommended:'Aanbevolen',sortLow:'Prijs laag → hoog',sortHigh:'Prijs hoog → laag',sortName:'Naam A → Z'},
 en:{sortRecommended:'Recommended',sortLow:'Price low → high',sortHigh:'Price high → low',sortName:'Name A → Z'},
 fr:{sortRecommended:'Recommandé',sortLow:'Prix croissant',sortHigh:'Prix décroissant',sortName:'Nom A → Z'},
 de:{sortRecommended:'Empfohlen',sortLow:'Preis aufsteigend',sortHigh:'Preis absteigend',sortName:'Name A → Z'},
 it:{sortRecommended:'Consigliato',sortLow:'Prezzo crescente',sortHigh:'Prezzo decrescente',sortName:'Nome A → Z'},
 es:{sortRecommended:'Recomendado',sortLow:'Precio menor → mayor',sortHigh:'Precio mayor → menor',sortName:'Nombre A → Z'}
};
Object.keys(sortTranslations).forEach(lang=>{translations[lang]={...(translations[lang]||{}),...sortTranslations[lang]};});

const contactTranslations={
 nl:{footerContactTitle:'Contact',footerContactText:'Heb je een vraag of feedback? Stuur ons een bericht.',contactName:'Naam',contactEmail:'E-mail',contactMessage:'Bericht',contactSubmit:'Verstuur bericht →'},
 en:{footerContactTitle:'Contact',footerContactText:'Have a question or feedback? Send us a message.',contactName:'Name',contactEmail:'Email',contactMessage:'Message',contactSubmit:'Send message →'},
 fr:{footerContactTitle:'Contact',footerContactText:'Une question ou un commentaire ? Envoyez-nous un message.',contactName:'Nom',contactEmail:'E-mail',contactMessage:'Message',contactSubmit:'Envoyer le message →'},
 de:{footerContactTitle:'Kontakt',footerContactText:'Haben Sie eine Frage oder Feedback? Senden Sie uns eine Nachricht.',contactName:'Name',contactEmail:'E-Mail',contactMessage:'Nachricht',contactSubmit:'Nachricht senden →'},
 it:{footerContactTitle:'Contatti',footerContactText:'Hai una domanda o un feedback? Inviaci un messaggio.',contactName:'Nome',contactEmail:'E-mail',contactMessage:'Messaggio',contactSubmit:'Invia messaggio →'},
 es:{footerContactTitle:'Contacto',footerContactText:'¿Tienes una pregunta o comentario? Envíanos un mensaje.',contactName:'Nombre',contactEmail:'Correo electrónico',contactMessage:'Mensaje',contactSubmit:'Enviar mensaje →'}
};
Object.keys(contactTranslations).forEach(lang=>{translations[lang]={...(translations[lang]||{}),...contactTranslations[lang]};});

/* Shared translations that were previously hard-coded in the footer/hero. */
const sharedTranslations={
 nl:{curatedPick:'GESELECTEERD',resultsFor:'resultaten voor',footerFaq:'Info',footerFaqLink:'Veelgestelde vragen',footerFaqLinkShort:'FAQ',footerAbout:'Over TrendMix',footerAffiliate:'Affiliate & transparantie',footerPrivacy:'Privacy',footerCookies:'Cookies & voorkeuren',footerBadgeMobile:'✓ Mobile first',footerBadgeLanguages:'✓ 6 talen',footerBadgeCollections:'✓ 5 collecties',footerBottom:'Modern · overzichtelijk · transparant · toegankelijk'},
 en:{curatedPick:'CURATED PICK',resultsFor:'results for',footerFaq:'Info',footerFaqLink:'Frequently asked questions',footerFaqLinkShort:'FAQ',footerAbout:'About TrendMix',footerAffiliate:'Affiliate & transparency',footerPrivacy:'Privacy',footerCookies:'Cookies & preferences',footerBadgeMobile:'✓ Mobile first',footerBadgeLanguages:'✓ 6 languages',footerBadgeCollections:'✓ 5 collections',footerBottom:'Modern · clear · transparent · accessible'},
 fr:{curatedPick:'SÉLECTION',resultsFor:'résultats pour',footerFaq:'Infos',footerFaqLink:'Questions fréquentes',footerFaqLinkShort:'FAQ',footerAbout:'À propos de TrendMix',footerAffiliate:'Affiliation & transparence',footerPrivacy:'Confidentialité',footerCookies:'Cookies & préférences',footerBadgeMobile:'✓ Mobile d’abord',footerBadgeLanguages:'✓ 6 langues',footerBadgeCollections:'✓ 5 collections',footerBottom:'Moderne · clair · transparent · accessible'},
 de:{curatedPick:'AUSGEWÄHLT',resultsFor:'Ergebnisse für',footerFaq:'Info',footerFaqLink:'Häufige Fragen',footerFaqLinkShort:'FAQ',footerAbout:'Über TrendMix',footerAffiliate:'Affiliate & Transparenz',footerPrivacy:'Datenschutz',footerCookies:'Cookies & Einstellungen',footerBadgeMobile:'✓ Mobile first',footerBadgeLanguages:'✓ 6 Sprachen',footerBadgeCollections:'✓ 5 Kollektionen',footerBottom:'Modern · übersichtlich · transparent · zugänglich'},
 it:{curatedPick:'SELEZIONATO',resultsFor:'risultati per',footerFaq:'Info',footerFaqLink:'Domande frequenti',footerFaqLinkShort:'FAQ',footerAbout:'Chi è TrendMix',footerAffiliate:'Affiliazione & trasparenza',footerPrivacy:'Privacy',footerCookies:'Cookie & preferenze',footerBadgeMobile:'✓ Mobile first',footerBadgeLanguages:'✓ 6 lingue',footerBadgeCollections:'✓ 5 collezioni',footerBottom:'Moderno · chiaro · trasparente · accessibile'},
 es:{curatedPick:'SELECCIÓN',resultsFor:'resultados para',footerFaq:'Info',footerFaqLink:'Preguntas frecuentes',footerFaqLinkShort:'FAQ',footerAbout:'Sobre TrendMix',footerAffiliate:'Afiliación y transparencia',footerPrivacy:'Privacidad',footerCookies:'Cookies y preferencias',footerBadgeMobile:'✓ Mobile first',footerBadgeLanguages:'✓ 6 idiomas',footerBadgeCollections:'✓ 5 colecciones',footerBottom:'Moderno · claro · transparente · accesible'}
};
Object.keys(sharedTranslations).forEach(lang=>{translations[lang]={...(translations[lang]||{}),...sharedTranslations[lang]};});

/* Category cards were server-rendered in Dutch and therefore stayed unchanged.
   Translate their names, eyebrow text and hero category whenever the language changes. */
const categoryTranslations={
 nl:{'pc-componenten':['PC-Componenten','Performance & gaming'],gadgets:['Gadgets','Slimme tech voor elke dag'],'smart-home':['Smart Home','Comfort & connected living'],'beauty-care':['Beauty & Care','Self-care & beauty'],'lifestyle-sport':['Sport & Lifestyle','Move, recover & live']},
 en:{'pc-componenten':['PC Components','Performance & gaming'],gadgets:['Gadgets','Smart tech for every day'],'smart-home':['Smart Home','Comfort & connected living'],'beauty-care':['Beauty & Care','Self-care & beauty'],'lifestyle-sport':['Sport & Lifestyle','Move, recover & live']},
 fr:{'pc-componenten':['Composants PC','Performance & gaming'],gadgets:['Gadgets','Technologie intelligente au quotidien'],'smart-home':['Maison connectée','Confort & vie connectée'],'beauty-care':['Beauté & soins','Soin de soi & beauté'],'lifestyle-sport':['Sport & lifestyle','Bouger, récupérer & vivre']},
 de:{'pc-componenten':['PC-Komponenten','Leistung & Gaming'],gadgets:['Gadgets','Smarte Technik für jeden Tag'],'smart-home':['Smart Home','Komfort & vernetztes Leben'],'beauty-care':['Beauty & Pflege','Self-Care & Beauty'],'lifestyle-sport':['Sport & Lifestyle','Bewegen, erholen & leben']},
 it:{'pc-componenten':['Componenti PC','Prestazioni & gaming'],gadgets:['Gadget','Tecnologia smart per ogni giorno'],'smart-home':['Casa intelligente','Comfort & vita connessa'],'beauty-care':['Beauty & cura','Self-care & bellezza'],'lifestyle-sport':['Sport & lifestyle','Muoversi, recuperare & vivere']},
 es:{'pc-componenten':['Componentes PC','Rendimiento y gaming'],gadgets:['Gadgets','Tecnología inteligente para cada día'],'smart-home':['Smart Home','Confort y vida conectada'],'beauty-care':['Belleza y cuidado','Cuidado personal y belleza'],'lifestyle-sport':['Deporte y lifestyle','Muévete, recupérate y vive']}
};

const originalApplyLanguage=applyLanguage;
applyLanguage=function(lang){
  originalApplyLanguage(lang);
  const cats=categoryTranslations[lang]||categoryTranslations.nl;
  document.querySelectorAll('[data-category-name]').forEach(el=>{
    const slug=el.dataset.categoryName;
    if(cats[slug]) el.textContent=cats[slug][0];
  });
  document.querySelectorAll('[data-category-eyebrow]').forEach(el=>{
    const slug=el.dataset.categoryEyebrow;
    if(cats[slug]) el.textContent=cats[slug][1];
  });

  Object.keys(cats).forEach(slug=>{
    const [name,eyebrow]=cats[slug];
    document.querySelectorAll('.nav-link[href="/'+slug+'"] span:last-child').forEach(el=>el.textContent=name);
    document.querySelectorAll('.category-card[href="/'+slug+'"] h3').forEach(el=>el.textContent=name);
    document.querySelectorAll('.category-card[href="/'+slug+'"] .category-content > div:last-child > span').forEach(el=>el.textContent=eyebrow);
  });
  const heroSmall=document.querySelector('.hero-card small');
  if(heroSmall){
    const current=heroSmall.textContent.trim();
    const heroSlug=Object.keys(categoryTranslations.nl).find(slug=>categoryTranslations.nl[slug][0]===current);
    if(heroSlug) heroSmall.textContent=cats[heroSlug][0];
  }
};


/* FAQ + information pages: client-side localized content for all six languages. */
const faqContent={
nl:[
['Wat is TrendMix?','TrendMix is een onafhankelijke productcatalogus waarmee je producten uit verschillende collecties kunt ontdekken. TrendMix verkoopt de producten zelf niet.'],
['Kan ik een product rechtstreeks bij TrendMix bestellen?','Nee. Je kunt worden doorgestuurd naar een externe aanbieder. Daar vindt de daadwerkelijke aankoop en betaling plaats.'],
['Waarom kan de prijs bij de aanbieder anders zijn?','Prijzen, aanbiedingen, voorraad en voorwaarden kunnen veranderen. Controleer daarom altijd de actuele informatie bij de externe aanbieder.'],
['Gebruikt TrendMix affiliate links?','Ja, sommige productlinks kunnen affiliate links zijn. TrendMix kan dan een commissie ontvangen zonder extra kosten voor jou.'],
['Heeft een affiliatecommissie invloed op de productinformatie?','TrendMix presenteert catalogusinformatie en gebruikt geen verzonnen reviews, beoordelingen of claims om een product aantrekkelijker te maken.'],
['Zijn de reviews op TrendMix echt?','TrendMix publiceert geen gefingeerde reviews. Als externe beoordelingen worden getoond, wordt duidelijk aangegeven waar deze vandaan komen.'],
['Wie is verantwoordelijk voor mijn bestelling?','De externe aanbieder waarbij je bestelt. Voor betaling, levering, garantie, retouren en klantenservice gelden de voorwaarden van die aanbieder.'],
['Kan ik een bestelling via TrendMix retourneren?','TrendMix verwerkt zelf geen bestellingen. Neem voor retourneren, annuleren of bestelvragen contact op met de externe aanbieder.'],
['Gebruikt TrendMix cookies?','TrendMix houdt cookies beperkt. Een lokale taalvoorkeur kan bijvoorbeeld in je browser worden opgeslagen. Externe websites kunnen eigen cookies gebruiken.'],
['Welke gegevens verzamelt TrendMix?','De catalogus kan zonder account worden bekeken. Voor meer informatie over gegevens en lokale voorkeuren kun je de privacy- en cookiepagina bekijken.'],
['Waarom staat een product niet meer online?','Producten kunnen veranderen, verdwijnen, uitverkocht raken of niet langer relevant zijn. Daarom wordt het aanbod regelmatig aangepast.'],
['Hoe kan ik een fout in productinformatie melden?','Gebruik de contactmogelijkheid op TrendMix. We kunnen de betreffende productinformatie controleren en waar nodig aanpassen.']
],
en:[
['What is TrendMix?','TrendMix is an independent product catalog for discovering products across different collections. TrendMix does not sell the products itself.'],
['Can I order a product directly from TrendMix?','No. You may be sent to an external retailer, where the purchase and payment take place.'],
['Why can the retailer price be different?','Prices, offers, stock and terms can change. Always check the current information with the external retailer.'],
['Does TrendMix use affiliate links?','Yes, some product links may be affiliate links. TrendMix may receive a commission at no extra cost to you.'],
['Does an affiliate commission affect product information?','TrendMix presents catalog information and does not use fabricated reviews, ratings or claims to make a product look more attractive.'],
['Are the reviews on TrendMix real?','TrendMix does not publish fabricated reviews. If external ratings are shown, their source will be clearly identified.'],
['Who is responsible for my order?','The external retailer where you place the order. Its terms apply to payment, delivery, warranty, returns and customer service.'],
['Can I return an order through TrendMix?','TrendMix does not process orders. For returns, cancellations or order questions, contact the external retailer.'],
['Does TrendMix use cookies?','TrendMix keeps cookies limited. A local language preference may be stored in your browser. External websites may use their own cookies.'],
['What data does TrendMix collect?','The catalog can be viewed without an account. See the privacy and cookie pages for more information about data and local preferences.'],
['Why is a product no longer online?','Products can change, disappear, sell out or become less relevant. The catalog may therefore be updated regularly.'],
['How can I report incorrect product information?','Use the contact option on TrendMix. We can review the product information and update it when needed.']
],
fr:[
['Qu’est-ce que TrendMix ?','TrendMix est un catalogue indépendant qui permet de découvrir des produits dans différentes collections. TrendMix ne vend pas directement les produits.'],
['Puis-je commander directement chez TrendMix ?','Non. Vous pouvez être redirigé vers un vendeur externe, où l’achat et le paiement sont effectués.'],
['Pourquoi le prix chez le vendeur peut-il être différent ?','Les prix, offres, stocks et conditions peuvent changer. Vérifiez toujours les informations actuelles chez le vendeur externe.'],
['TrendMix utilise-t-il des liens affiliés ?','Oui, certains liens peuvent être affiliés. TrendMix peut recevoir une commission sans coût supplémentaire pour vous.'],
['Une commission d’affiliation influence-t-elle les informations produit ?','TrendMix présente des informations de catalogue et n’utilise pas de faux avis, notes ou affirmations pour rendre un produit plus attractif.'],
['Les avis sur TrendMix sont-ils réels ?','TrendMix ne publie pas de faux avis. Si des évaluations externes sont affichées, leur source sera clairement indiquée.'],
['Qui est responsable de ma commande ?','Le vendeur externe auprès duquel vous commandez. Ses conditions s’appliquent au paiement, à la livraison, à la garantie, aux retours et au service client.'],
['Puis-je retourner une commande via TrendMix ?','TrendMix ne traite pas les commandes. Pour un retour, une annulation ou une question, contactez le vendeur externe.'],
['TrendMix utilise-t-il des cookies ?','TrendMix limite les cookies. Une préférence de langue locale peut être enregistrée dans votre navigateur. Les sites externes peuvent utiliser leurs propres cookies.'],
['Quelles données TrendMix collecte-t-il ?','Le catalogue peut être consulté sans compte. Consultez les pages confidentialité et cookies pour plus d’informations.'],
['Pourquoi un produit n’est-il plus en ligne ?','Les produits peuvent changer, disparaître, être épuisés ou devenir moins pertinents. Le catalogue peut donc être mis à jour régulièrement.'],
['Comment signaler une information produit incorrecte ?','Utilisez le moyen de contact disponible sur TrendMix. Nous pouvons vérifier les informations et les corriger si nécessaire.']
],
de:[
['Was ist TrendMix?','TrendMix ist ein unabhängiger Produktkatalog, mit dem du Produkte aus verschiedenen Kollektionen entdecken kannst. TrendMix verkauft die Produkte nicht selbst.'],
['Kann ich ein Produkt direkt bei TrendMix bestellen?','Nein. Du kannst zu einem externen Anbieter weitergeleitet werden, bei dem Kauf und Zahlung stattfinden.'],
['Warum kann der Preis beim Anbieter anders sein?','Preise, Angebote, Lagerbestand und Bedingungen können sich ändern. Prüfe immer die aktuellen Angaben beim externen Anbieter.'],
['Verwendet TrendMix Affiliate-Links?','Ja, einige Produktlinks können Affiliate-Links sein. TrendMix kann dafür eine Provision erhalten, ohne zusätzliche Kosten für dich.'],
['Beeinflusst eine Affiliate-Provision die Produktinformationen?','TrendMix stellt Kataloginformationen bereit und verwendet keine erfundenen Bewertungen oder Behauptungen, um Produkte attraktiver erscheinen zu lassen.'],
['Sind die Bewertungen auf TrendMix echt?','TrendMix veröffentlicht keine erfundenen Bewertungen. Wenn externe Bewertungen angezeigt werden, wird ihre Quelle klar genannt.'],
['Wer ist für meine Bestellung verantwortlich?','Der externe Anbieter, bei dem du bestellst. Dessen Bedingungen gelten für Zahlung, Lieferung, Garantie, Rückgabe und Kundenservice.'],
['Kann ich eine Bestellung über TrendMix zurückgeben?','TrendMix verarbeitet keine Bestellungen. Für Rückgaben, Stornierungen oder Bestellfragen wende dich an den externen Anbieter.'],
['Verwendet TrendMix Cookies?','TrendMix hält Cookies begrenzt. Eine lokale Sprachpräferenz kann im Browser gespeichert werden. Externe Websites können eigene Cookies verwenden.'],
['Welche Daten sammelt TrendMix?','Der Katalog kann ohne Konto genutzt werden. Weitere Informationen zu Daten und lokalen Einstellungen findest du auf den Datenschutz- und Cookie-Seiten.'],
['Warum ist ein Produkt nicht mehr online?','Produkte können sich ändern, verschwinden, ausverkauft sein oder weniger relevant werden. Der Katalog wird deshalb regelmäßig angepasst.'],
['Wie kann ich falsche Produktinformationen melden?','Nutze die Kontaktmöglichkeit auf TrendMix. Wir können die Informationen prüfen und bei Bedarf anpassen.']
],
it:[
['Cos’è TrendMix?','TrendMix è un catalogo indipendente per scoprire prodotti di diverse collezioni. TrendMix non vende direttamente i prodotti.'],
['Posso ordinare un prodotto direttamente da TrendMix?','No. Potresti essere reindirizzato a un venditore esterno, dove avvengono acquisto e pagamento.'],
['Perché il prezzo del venditore può essere diverso?','Prezzi, offerte, disponibilità e condizioni possono cambiare. Controlla sempre le informazioni aggiornate presso il venditore esterno.'],
['TrendMix usa link affiliati?','Sì, alcuni link possono essere affiliati. TrendMix può ricevere una commissione senza costi aggiuntivi per te.'],
['Una commissione di affiliazione influenza le informazioni sui prodotti?','TrendMix presenta informazioni di catalogo e non usa recensioni, valutazioni o affermazioni inventate per rendere un prodotto più attraente.'],
['Le recensioni su TrendMix sono reali?','TrendMix non pubblica recensioni inventate. Se vengono mostrate valutazioni esterne, la loro fonte sarà indicata chiaramente.'],
['Chi è responsabile del mio ordine?','Il venditore esterno presso cui effettui l’ordine. Le sue condizioni regolano pagamento, consegna, garanzia, resi e assistenza.'],
['Posso restituire un ordine tramite TrendMix?','TrendMix non gestisce gli ordini. Per resi, cancellazioni o domande sull’ordine, contatta il venditore esterno.'],
['TrendMix usa i cookie?','TrendMix limita i cookie. Una preferenza linguistica locale può essere salvata nel browser. I siti esterni possono usare i propri cookie.'],
['Quali dati raccoglie TrendMix?','Il catalogo può essere consultato senza account. Per maggiori informazioni, consulta le pagine privacy e cookie.'],
['Perché un prodotto non è più online?','I prodotti possono cambiare, sparire, esaurirsi o diventare meno rilevanti. Il catalogo può quindi essere aggiornato regolarmente.'],
['Come posso segnalare informazioni errate su un prodotto?','Usa il contatto disponibile su TrendMix. Possiamo verificare le informazioni e aggiornarle quando necessario.']
],
es:[
['¿Qué es TrendMix?','TrendMix es un catálogo independiente para descubrir productos de distintas colecciones. TrendMix no vende los productos directamente.'],
['¿Puedo pedir un producto directamente a TrendMix?','No. Puedes ser enviado a un vendedor externo, donde se realizan la compra y el pago.'],
['¿Por qué puede ser diferente el precio del vendedor?','Los precios, ofertas, existencias y condiciones pueden cambiar. Comprueba siempre la información actual con el vendedor externo.'],
['¿TrendMix utiliza enlaces de afiliados?','Sí, algunos enlaces pueden ser de afiliados. TrendMix puede recibir una comisión sin coste adicional para ti.'],
['¿Una comisión de afiliación influye en la información del producto?','TrendMix presenta información de catálogo y no utiliza reseñas, valoraciones o afirmaciones inventadas para hacer más atractivo un producto.'],
['¿Las reseñas de TrendMix son reales?','TrendMix no publica reseñas inventadas. Si se muestran valoraciones externas, se indicará claramente su origen.'],
['¿Quién es responsable de mi pedido?','El vendedor externo donde realizas el pedido. Sus condiciones se aplican al pago, entrega, garantía, devoluciones y atención al cliente.'],
['¿Puedo devolver un pedido a través de TrendMix?','TrendMix no gestiona pedidos. Para devoluciones, cancelaciones o dudas sobre el pedido, contacta con el vendedor externo.'],
['¿TrendMix utiliza cookies?','TrendMix limita las cookies. El navegador puede guardar una preferencia de idioma local. Los sitios externos pueden usar sus propias cookies.'],
['¿Qué datos recopila TrendMix?','El catálogo puede consultarse sin cuenta. Consulta las páginas de privacidad y cookies para más información.'],
['¿Por qué un producto ya no está disponible en línea?','Los productos pueden cambiar, desaparecer, agotarse o dejar de ser relevantes. El catálogo puede actualizarse periódicamente.'],
['¿Cómo puedo informar de un error en la información de un producto?','Usa la opción de contacto de TrendMix. Podemos revisar la información y actualizarla cuando sea necesario.']
]};

const infoContent={
nl:{
'over-trendmix':{title:'Over TrendMix',desc:'Hoe TrendMix werkt als onafhankelijke productcatalogus.',html:'<p>TrendMix is een onafhankelijke productcatalogus voor moderne trends in tech, home, beauty en lifestyle. We brengen producten overzichtelijk samen zodat je sneller kunt ontdekken wat interessant is.</p><h2>Geen gewone webshop</h2><p>TrendMix is ingericht als discovery- en affiliateplatform. Een aankoop wordt niet bij TrendMix afgerekend: wanneer je op een productdoorgang klikt, kun je worden doorgestuurd naar een externe aanbieder.</p><h2>Prijzen en beschikbaarheid</h2><p>Productprijzen, voorraad, levering en voorwaarden kunnen veranderen. Controleer daarom altijd de actuele informatie bij de externe aanbieder voordat je bestelt.</p>'},
'affiliate':{title:'Affiliate & transparantie',desc:'Transparantie over affiliate links en commerciële relaties bij TrendMix.',html:'<p><strong>TrendMix kan affiliate links gebruiken.</strong> Als je via zo’n link bij een externe aanbieder een aankoop doet, kan TrendMix daarvoor een commissie ontvangen. De commissie verandert jouw prijs niet.</p><h2>Waarom melden we dit?</h2><p>We willen duidelijk maken wanneer een productdoorgang commercieel kan zijn. Reclame en commerciële relaties horen herkenbaar en transparant te zijn.</p><h2>Onze productinformatie</h2><p>TrendMix gebruikt catalogusinformatie om producten te presenteren. Controleer voor aankoop altijd de actuele prijs, voorraad, specificaties, levering en retourvoorwaarden bij de aanbieder.</p><h2>Reviews</h2><p>TrendMix presenteert geen verzonnen reviews of beoordelingen. Wanneer er in de toekomst externe beoordelingen worden getoond, moet duidelijk zijn waar deze vandaan komen.</p>'},
'privacy':{title:'Privacy',desc:'Privacyinformatie voor bezoekers van TrendMix.',html:'<p>TrendMix is opgezet als een eenvoudige productcatalogus. We vragen op dit moment geen account aan om de catalogus te bekijken.</p><h2>Taalvoorkeur</h2><p>De gekozen taal kan lokaal in je browser worden opgeslagen zodat TrendMix je voorkeur bij een volgend bezoek kan onthouden.</p><h2>Externe aanbieders</h2><p>Wanneer je TrendMix verlaat via een product- of affiliate link, geldt het privacybeleid van de externe website die je bezoekt. Lees daar de voorwaarden voordat je gegevens achterlaat of een aankoop doet.</p><h2>Wijzigingen</h2><p>Deze informatie kan worden aangepast wanneer de functies van TrendMix veranderen.</p>'},
'cookies':{title:'Cookies & voorkeuren',desc:'Informatie over cookies en lokale voorkeuren op TrendMix.',html:'<p>TrendMix houdt de site bewust eenvoudig. De huidige taalkeuze kan lokaal in je browser worden bewaard. Dit is een lokale voorkeur en geen TrendMix-account.</p><h2>Externe websites</h2><p>Externe aanbieders kunnen hun eigen cookies, analytics of advertentietechnieken gebruiken nadat je TrendMix verlaat. Controleer daarvoor het cookie- en privacybeleid van die aanbieder.</p><h2>Voorkeur wissen</h2><p>Je kunt lokale sitegegevens in de instellingen van je browser wissen. Daarna wordt de standaardtaal opnieuw gebruikt.</p>'}},
en:{
'over-trendmix':{title:'About TrendMix',desc:'How TrendMix works as an independent product catalog.',html:'<p>TrendMix is an independent product catalog for modern trends in tech, home, beauty and lifestyle. We bring products together clearly so you can discover what is interesting faster.</p><h2>Not a regular webshop</h2><p>TrendMix is designed as a discovery and affiliate platform. Purchases are not completed on TrendMix; clicking a product link may take you to an external retailer.</p><h2>Prices and availability</h2><p>Prices, stock, delivery and terms can change. Always check the current information with the external retailer before ordering.</p>'},
'affiliate':{title:'Affiliate & transparency',desc:'Transparency about affiliate links and commercial relationships at TrendMix.',html:'<p><strong>TrendMix may use affiliate links.</strong> If you purchase through such a link, TrendMix may receive a commission. This does not change your price.</p><h2>Why disclose this?</h2><p>We want to make clear when a product link may have a commercial relationship behind it. Commercial relationships should be recognizable and transparent.</p><h2>Our product information</h2><p>TrendMix uses catalog information to present products. Before buying, always check current price, stock, specifications, delivery and return terms with the retailer.</p><h2>Reviews</h2><p>TrendMix does not present fabricated reviews or ratings. If external ratings are shown in the future, their source should be clearly identified.</p>'},
'privacy':{title:'Privacy',desc:'Privacy information for TrendMix visitors.',html:'<p>TrendMix is designed as a simple product catalog. No account is currently required to browse the catalog.</p><h2>Language preference</h2><p>Your selected language may be stored locally in your browser so TrendMix can remember it on a later visit.</p><h2>External retailers</h2><p>When you leave TrendMix through a product or affiliate link, the privacy policy of the external website applies. Review its terms before submitting information or making a purchase.</p><h2>Changes</h2><p>This information may be updated when TrendMix features change.</p>'},
'cookies':{title:'Cookies & preferences',desc:'Information about cookies and local preferences on TrendMix.',html:'<p>TrendMix keeps the site simple. Your current language choice may be stored locally in your browser. This is a local preference, not a TrendMix account.</p><h2>External websites</h2><p>External retailers may use their own cookies, analytics or advertising technologies after you leave TrendMix. Check their privacy and cookie policies.</p><h2>Clear preference</h2><p>You can clear local site data in your browser settings. The default language will then be used again.</p>'}},
fr:{
'over-trendmix':{title:'À propos de TrendMix',desc:'Comment TrendMix fonctionne comme catalogue indépendant.',html:'<p>TrendMix est un catalogue indépendant consacré aux tendances tech, maison, beauté et lifestyle. Nous réunissons les produits clairement pour faciliter la découverte.</p><h2>Pas une boutique classique</h2><p>TrendMix est une plateforme de découverte et d’affiliation. Les achats ne sont pas effectués sur TrendMix ; un lien produit peut vous rediriger vers un vendeur externe.</p><h2>Prix et disponibilité</h2><p>Les prix, stocks, livraisons et conditions peuvent changer. Vérifiez toujours les informations actuelles auprès du vendeur externe.</p>'},
'affiliate':{title:'Affiliation & transparence',desc:'Transparence sur les liens affiliés et relations commerciales de TrendMix.',html:'<p><strong>TrendMix peut utiliser des liens affiliés.</strong> Si vous achetez via un tel lien, TrendMix peut recevoir une commission. Votre prix ne change pas.</p><h2>Pourquoi le préciser ?</h2><p>Nous voulons indiquer clairement lorsqu’un lien produit peut avoir une relation commerciale. Les relations commerciales doivent rester reconnaissables et transparentes.</p><h2>Informations produits</h2><p>TrendMix utilise des informations de catalogue. Avant tout achat, vérifiez le prix, le stock, les caractéristiques, la livraison et les retours auprès du vendeur.</p><h2>Avis</h2><p>TrendMix ne publie pas de faux avis ou évaluations. Si des évaluations externes sont affichées, leur source doit être clairement indiquée.</p>'},
'privacy':{title:'Confidentialité',desc:'Informations de confidentialité pour les visiteurs de TrendMix.',html:'<p>TrendMix est conçu comme un catalogue simple. Aucun compte n’est actuellement nécessaire pour consulter le catalogue.</p><h2>Préférence de langue</h2><p>La langue choisie peut être enregistrée localement dans votre navigateur afin d’être mémorisée lors d’une prochaine visite.</p><h2>Vendeurs externes</h2><p>Lorsque vous quittez TrendMix via un lien produit ou affilié, la politique de confidentialité du site externe s’applique.</p><h2>Modifications</h2><p>Ces informations peuvent être mises à jour lorsque les fonctions de TrendMix évoluent.</p>'},
'cookies':{title:'Cookies & préférences',desc:'Informations sur les cookies et préférences locales de TrendMix.',html:'<p>TrendMix reste volontairement simple. Le choix de langue peut être enregistré localement dans votre navigateur. Il s’agit d’une préférence locale, pas d’un compte TrendMix.</p><h2>Sites externes</h2><p>Les vendeurs externes peuvent utiliser leurs propres cookies, outils d’analyse ou technologies publicitaires. Consultez leurs politiques.</p><h2>Effacer la préférence</h2><p>Vous pouvez supprimer les données locales dans les paramètres de votre navigateur. La langue par défaut sera alors utilisée.</p>'}},
de:{
'over-trendmix':{title:'Über TrendMix',desc:'Wie TrendMix als unabhängiger Produktkatalog funktioniert.',html:'<p>TrendMix ist ein unabhängiger Produktkatalog für moderne Trends in Technik, Home, Beauty und Lifestyle. Wir bündeln Produkte übersichtlich, damit du schneller entdecken kannst, was interessant ist.</p><h2>Kein gewöhnlicher Webshop</h2><p>TrendMix ist als Discovery- und Affiliate-Plattform aufgebaut. Käufe werden nicht bei TrendMix abgeschlossen; ein Produktlink kann zu einem externen Anbieter führen.</p><h2>Preise und Verfügbarkeit</h2><p>Preise, Bestand, Lieferung und Bedingungen können sich ändern. Prüfe vor dem Kauf immer die aktuellen Angaben beim externen Anbieter.</p>'},
'affiliate':{title:'Affiliate & Transparenz',desc:'Transparenz über Affiliate-Links und kommerzielle Beziehungen bei TrendMix.',html:'<p><strong>TrendMix kann Affiliate-Links verwenden.</strong> Wenn du über einen solchen Link kaufst, kann TrendMix eine Provision erhalten. Dein Preis ändert sich dadurch nicht.</p><h2>Warum weisen wir darauf hin?</h2><p>Wir möchten klar machen, wenn hinter einem Produktlink eine kommerzielle Beziehung stehen kann.</p><h2>Produktinformationen</h2><p>TrendMix nutzt Kataloginformationen. Prüfe vor dem Kauf immer Preis, Bestand, Spezifikationen, Lieferung und Rückgabebedingungen beim Anbieter.</p><h2>Bewertungen</h2><p>TrendMix veröffentlicht keine erfundenen Bewertungen. Wenn externe Bewertungen gezeigt werden, wird ihre Quelle klar angegeben.</p>'},
'privacy':{title:'Datenschutz',desc:'Datenschutzinformationen für TrendMix-Besucher.',html:'<p>TrendMix ist als einfacher Produktkatalog aufgebaut. Für das Durchsuchen des Katalogs ist derzeit kein Konto erforderlich.</p><h2>Sprachpräferenz</h2><p>Die gewählte Sprache kann lokal im Browser gespeichert werden, damit TrendMix sie beim nächsten Besuch wieder verwendet.</p><h2>Externe Anbieter</h2><p>Wenn du TrendMix über einen Produkt- oder Affiliate-Link verlässt, gilt die Datenschutzrichtlinie der externen Website.</p><h2>Änderungen</h2><p>Diese Informationen können aktualisiert werden, wenn sich Funktionen von TrendMix ändern.</p>'},
'cookies':{title:'Cookies & Einstellungen',desc:'Informationen zu Cookies und lokalen Einstellungen bei TrendMix.',html:'<p>TrendMix bleibt bewusst einfach. Die gewählte Sprache kann lokal im Browser gespeichert werden. Dies ist eine lokale Einstellung und kein TrendMix-Konto.</p><h2>Externe Websites</h2><p>Externe Anbieter können eigene Cookies, Analyse- oder Werbetechniken verwenden. Prüfe deren Datenschutz- und Cookie-Richtlinien.</p><h2>Einstellung löschen</h2><p>Lokale Websitedaten kannst du in den Browsereinstellungen löschen. Danach wird wieder die Standardsprache verwendet.</p>'}},
it:{
'over-trendmix':{title:'Chi è TrendMix',desc:'Come funziona TrendMix come catalogo indipendente.',html:'<p>TrendMix è un catalogo indipendente dedicato alle tendenze tech, casa, beauty e lifestyle. Riuniamo i prodotti in modo chiaro per aiutarti a scoprire più velocemente ciò che interessa.</p><h2>Non è un normale negozio online</h2><p>TrendMix è una piattaforma di scoperta e affiliazione. Gli acquisti non vengono completati su TrendMix; un link può portarti a un venditore esterno.</p><h2>Prezzi e disponibilità</h2><p>Prezzi, disponibilità, consegna e condizioni possono cambiare. Controlla sempre le informazioni aggiornate presso il venditore.</p>'},
'affiliate':{title:'Affiliazione & trasparenza',desc:'Trasparenza sui link affiliati e sui rapporti commerciali di TrendMix.',html:'<p><strong>TrendMix può usare link affiliati.</strong> Se acquisti tramite uno di questi link, TrendMix può ricevere una commissione. Il tuo prezzo non cambia.</p><h2>Perché indicarlo?</h2><p>Vogliamo chiarire quando un link prodotto può avere un rapporto commerciale. I rapporti commerciali devono essere riconoscibili e trasparenti.</p><h2>Informazioni sui prodotti</h2><p>TrendMix usa informazioni di catalogo. Prima dell’acquisto controlla sempre prezzo, disponibilità, specifiche, consegna e resi presso il venditore.</p><h2>Recensioni</h2><p>TrendMix non presenta recensioni inventate. Se in futuro saranno mostrate valutazioni esterne, la loro fonte sarà indicata chiaramente.</p>'},
'privacy':{title:'Privacy',desc:'Informazioni sulla privacy per i visitatori di TrendMix.',html:'<p>TrendMix è un catalogo semplice. Al momento non è necessario un account per consultarlo.</p><h2>Preferenza linguistica</h2><p>La lingua scelta può essere salvata localmente nel browser per ricordarla alla visita successiva.</p><h2>Venditori esterni</h2><p>Quando lasci TrendMix tramite un link prodotto o affiliato, si applica la privacy policy del sito esterno.</p><h2>Modifiche</h2><p>Queste informazioni possono essere aggiornate quando cambiano le funzioni di TrendMix.</p>'},
'cookies':{title:'Cookie & preferenze',desc:'Informazioni sui cookie e sulle preferenze locali di TrendMix.',html:'<p>TrendMix mantiene il sito semplice. La lingua scelta può essere salvata localmente nel browser. È una preferenza locale, non un account TrendMix.</p><h2>Siti esterni</h2><p>I venditori esterni possono usare cookie, analytics o tecnologie pubblicitarie proprie. Consulta le loro policy.</p><h2>Cancellare la preferenza</h2><p>Puoi cancellare i dati locali nelle impostazioni del browser. Verrà quindi usata di nuovo la lingua predefinita.</p>'}},
es:{
'over-trendmix':{title:'Sobre TrendMix',desc:'Cómo funciona TrendMix como catálogo independiente.',html:'<p>TrendMix es un catálogo independiente de tendencias en tecnología, hogar, belleza y lifestyle. Reunimos productos de forma clara para facilitar el descubrimiento.</p><h2>No es una tienda online convencional</h2><p>TrendMix funciona como plataforma de descubrimiento y afiliación. Las compras no se realizan en TrendMix; un enlace de producto puede llevarte a un vendedor externo.</p><h2>Precios y disponibilidad</h2><p>Los precios, existencias, entregas y condiciones pueden cambiar. Comprueba siempre la información actual con el vendedor externo.</p>'},
'affiliate':{title:'Afiliación y transparencia',desc:'Transparencia sobre enlaces de afiliados y relaciones comerciales en TrendMix.',html:'<p><strong>TrendMix puede utilizar enlaces de afiliados.</strong> Si compras mediante uno de ellos, TrendMix puede recibir una comisión. Tu precio no cambia.</p><h2>¿Por qué lo indicamos?</h2><p>Queremos dejar claro cuándo un enlace de producto puede tener una relación comercial. Estas relaciones deben ser reconocibles y transparentes.</p><h2>Información de productos</h2><p>TrendMix utiliza información de catálogo. Antes de comprar, comprueba siempre precio, existencias, especificaciones, entrega y devoluciones con el vendedor.</p><h2>Reseñas</h2><p>TrendMix no presenta reseñas inventadas. Si se muestran valoraciones externas, se indicará claramente su origen.</p>'},
'privacy':{title:'Privacidad',desc:'Información de privacidad para visitantes de TrendMix.',html:'<p>TrendMix está diseñado como un catálogo sencillo. Actualmente no se necesita una cuenta para consultarlo.</p><h2>Preferencia de idioma</h2><p>El idioma elegido puede guardarse localmente en el navegador para recordarlo en una visita posterior.</p><h2>Vendedores externos</h2><p>Al salir de TrendMix mediante un enlace de producto o afiliado, se aplica la política de privacidad del sitio externo.</p><h2>Cambios</h2><p>Esta información puede actualizarse cuando cambien las funciones de TrendMix.</p>'},
'cookies':{title:'Cookies y preferencias',desc:'Información sobre cookies y preferencias locales en TrendMix.',html:'<p>TrendMix mantiene el sitio sencillo. El idioma elegido puede guardarse localmente en el navegador. Es una preferencia local, no una cuenta de TrendMix.</p><h2>Sitios externos</h2><p>Los vendedores externos pueden utilizar sus propias cookies, analítica o tecnologías publicitarias. Consulta sus políticas.</p><h2>Borrar la preferencia</h2><p>Puedes borrar los datos locales del sitio en la configuración del navegador. Después se usará de nuevo el idioma predeterminado.</p>'}}
};

const pageUiTranslations={
nl:{faqTitle:'Veelgestelde vragen',faqLead:'Hier vind je praktische informatie over TrendMix, productlinks, prijzen en het aankoopproces.',backToTrendmix:'← Terug naar TrendMix'},
en:{faqTitle:'Frequently asked questions',faqLead:'Practical information about TrendMix, product links, prices and the buying process.',backToTrendmix:'← Back to TrendMix'},
fr:{faqTitle:'Questions fréquentes',faqLead:'Informations pratiques sur TrendMix, les liens produits, les prix et le processus d’achat.',backToTrendmix:'← Retour à TrendMix'},
de:{faqTitle:'Häufige Fragen',faqLead:'Praktische Informationen zu TrendMix, Produktlinks, Preisen und dem Kaufprozess.',backToTrendmix:'← Zurück zu TrendMix'},
it:{faqTitle:'Domande frequenti',faqLead:'Informazioni pratiche su TrendMix, link ai prodotti, prezzi e processo di acquisto.',backToTrendmix:'← Torna a TrendMix'},
es:{faqTitle:'Preguntas frecuentes',faqLead:'Información práctica sobre TrendMix, enlaces de productos, precios y proceso de compra.',backToTrendmix:'← Volver a TrendMix'}
};
Object.keys(pageUiTranslations).forEach(lang=>{translations[lang]={...(translations[lang]||{}),...pageUiTranslations[lang]};});

const baseApplyLanguage=applyLanguage;
applyLanguage=function(lang){
  baseApplyLanguage(lang);
  const faq=faqContent[lang]||faqContent.nl;
  document.querySelectorAll('[data-faq-item]').forEach((el,i)=>{
    if(faq[i]){el.querySelector('summary').textContent=faq[i][0];el.querySelector('p').textContent=faq[i][1];}
  });
  const slug=document.querySelector('[data-info-content]')?.dataset.infoContent;
  if(slug){
    const page=(infoContent[lang]||infoContent.nl)[slug]||(infoContent.nl)[slug];
    const contentEl=document.querySelector('[data-info-content]');
    const titleEl=document.querySelector('[data-info-title]');
    if(page){if(contentEl) contentEl.innerHTML=page.html;if(titleEl) titleEl.textContent=page.title;document.title=page.title+' | TrendMix';const meta=document.querySelector('[data-meta-description]');if(meta)meta.setAttribute('content',page.desc);}
  }else if(document.querySelector('[data-faq-item]')){
    const ui=pageUiTranslations[lang]||pageUiTranslations.nl;
    document.title=ui.faqTitle+' | TrendMix';
    const meta=document.querySelector('[data-meta-description]');if(meta)meta.setAttribute('content',ui.faqLead);
  }
};
