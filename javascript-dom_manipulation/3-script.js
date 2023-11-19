const headerTag = document.querySelector('header');
const toggleTag = document.querySelector('#toggle_header');

toggleTag.addEventListener('click', changeClass);

function changeClass(){
  headerTag.classList.toggle('red');
  headerTag.classList.toggle('green');
}
