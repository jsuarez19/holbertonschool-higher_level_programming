const characterTag = document.querySelector('#character');
const moviesList = document.querySelector('#list_movies')

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    movies.forEach(movies => {
      const newItem = document.createElement('li');
      newItem.textContent = movies.title;
      moviesList.appendChild(newItem);
    });
  })
