/* Small release pass for remaining dynamic labels outside the main translation dictionary. */
(function(){
  const t={
    nl:{recommended:'Aanbevolen',low:'Prijs laag → hoog',high:'Prijs hoog → laag',name:'Naam A → Z',results:'resultaten voor'},
    en:{recommended:'Recommended',low:'Price low → high',high:'Price high → low',name:'Name A → Z',results:'results for'},
    fr:{recommended:'Recommandé',low:'Prix croissant',high:'Prix décroissant',name:'Nom A → Z',results:'résultats pour'},
    de:{recommended:'Empfohlen',low:'Preis aufsteigend',high:'Preis absteigend',name:'Name A → Z',results:'Ergebnisse für'},
    it:{recommended:'Consigliato',low:'Prezzo crescente',high:'Prezzo decrescente',name:'Nome A → Z',results:'risultati per'},
    es:{recommended:'Recomendado',low:'Precio menor → mayor',high:'Precio mayor → menor',name:'Nombre A → Z',results:'resultados para'}
  };
  function apply(){
    const l=localStorage.getItem('trendmix-language')||'nl', x=t[l]||t.nl;
    const values=['recommended','price-low','price-high','name'];
    document.querySelectorAll('[data-sort-products] option').forEach((o,i)=>{if(values[i])o.textContent=x[values[i]==='price-low'?'low':values[i]==='price-high'?'high':values[i]]||o.textContent});
    document.querySelectorAll('[data-search-summary]').forEach(el=>{const n=el.dataset.results||'0';const q=el.dataset.query||'';el.textContent=n+' '+x.results+' “'+q+'”'});
  }
  document.addEventListener('DOMContentLoaded',()=>{apply();const s=document.getElementById('languageSelect');if(s)s.addEventListener('change',()=>setTimeout(apply,0));});
})();
