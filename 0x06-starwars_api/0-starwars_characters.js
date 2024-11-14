#!/usr/bin/node

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharacters(characters);
  } else {
    console.error(error);
  }
});

function printCharacters (characters) {
  (async () => {
    for (const characterUrl of characters) {
      try {
        const characterResponse = await requestPromise(characterUrl);
        const characterData = JSON.parse(characterResponse.body);
        console.log(characterData.name);
      } catch (err) {
        console.error(err);
      }
    }
  })();
}
