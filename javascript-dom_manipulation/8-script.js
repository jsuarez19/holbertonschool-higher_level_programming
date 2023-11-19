document.addEventListener('DOMContentLoaded', function (){
  const helloTag = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const translation = data.hello;
      helloTag.textContent = translation;
    });
})
