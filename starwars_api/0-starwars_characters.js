#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  let completed = 0;
  const names = {};

  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }

      const character = JSON.parse(body);
      names[index] = character.name;
      completed++;

      if (completed === characters.length) {
        for (let i = 0; i < characters.length; i++) {
          console.log(names[i]);
        }
      }
    });
  });
});
