const headerTag = document.querySelector('header');
const redHeaderTag = document.querySelector('#red_header');

redHeaderTag.addEventListener('click', addClass);

function addClass(){
  headerTag.classList.add('red')
}
