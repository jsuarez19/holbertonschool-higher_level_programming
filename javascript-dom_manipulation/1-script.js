const headerTag = document.querySelector('header');
const redHeaderTag = document.querySelector('#red_header');

redHeaderTag.addEventListener('click', changeColor);

function changeColor(){
  headerTag.style.color = '#FF0000'
}
