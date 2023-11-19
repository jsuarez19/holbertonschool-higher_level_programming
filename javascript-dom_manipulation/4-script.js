const addItemTag = document.querySelector('#add_item');

addItemTag.addEventListener('click', liCreate);

function liCreate(){
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  document.querySelector('.my_list').appendChild(newItem);
}
