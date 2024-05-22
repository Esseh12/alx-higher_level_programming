#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (error, response) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(response.body);
  const films = data.results;
  const episodeId = parseInt(process.argv[2], 10);
  for (const film of films) {
    if (film.episode_id === episodeId) {
      console.log(film.title);
      break;
    }
  }
});
