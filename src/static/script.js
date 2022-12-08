const form = document.querySelector('form');
const img = document.querySelector('img');
const fileInput = document.querySelector('input[type="file"]');
const label = document.querySelector('label[for="file-upload"]');

fileInput.addEventListener('input', () => {
    label.textContent = 'file chosen'
})

form.addEventListener('submit', e => {
    e.preventDefault();
    fetch('/files', {
        method: 'POST',
        body: new FormData(form)
    }).then(d => d.json()).then(data => {
        img.src = data.url
        label.textContent = 'go again?'
    });
})