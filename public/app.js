// регистрация service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(() => console.log('SW registered'))
      .catch(err => console.error('SW error', err));
  });
}

// загрузка книг
const list = document.getElementById('list');

async function loadBooks() {
  const author = document.getElementById('author').value.trim();
  const year = document.getElementById('year').value.trim();

  const params = new URLSearchParams();
  if (author) params.set('author', author);
  if (year) params.set('year', year);

  try {
    const res = await fetch('/api/books?' + params.toString());
    const books = await res.json();
    list.innerHTML = books.length
      ? books.map(b => `<li>${b.title} - ${b.author}, ${b.year}</li>`).join('')
      : '<li>Ничего не найдено</li>';
  } catch (e) {
    list.innerHTML = '<li>Нет соединения</li>';
  }
}

if (list) {
  document.getElementById('search').addEventListener('click', loadBooks);
  loadBooks();
}