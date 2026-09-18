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
