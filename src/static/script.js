const form = document.querySelector('form');
const img = document.querySelector('img');
form.addEventListener('submit', e => {
    e.preventDefault();
    fetch('/files', {
        method: 'POST',
        body: new FormData(form)
    }).then(d => d.json()).then(data => img.src = data.url);
})