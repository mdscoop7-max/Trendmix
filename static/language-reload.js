/* Ensure every translated layer re-runs after a language switch. */
document.addEventListener('DOMContentLoaded', () => {
  const select = document.getElementById('languageSelect');
  if (!select) return;
  select.addEventListener('change', () => {
    // app.js stores the selected language first; reload lets all i18n layers
    // (category labels, footer links and info pages) initialize from that value.
    setTimeout(() => window.location.reload(), 0);
  });
});
