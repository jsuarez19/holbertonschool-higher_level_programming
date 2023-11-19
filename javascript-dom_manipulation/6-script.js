const characterTag = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;
    characterTag.textContent = characterName;
  })
