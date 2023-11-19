const headerTag = document.querySelector('header');
const updateHeaderTag = document.querySelector('#update_header');

updateHeaderTag.addEventListener('click', updateText);

function updateText(){
  headerTag.textContent = 'New Header!!!'
}
