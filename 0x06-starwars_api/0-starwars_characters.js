#!/usr/bin/node

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, async function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    try {
      for (const characterUrl of characters) {
        const characterResponse = await requestPromise(characterUrl);
        const characterData = JSON.parse(characterResponse.body);
        console.log(characterData.name);
      }
    } catch (err) {
      console.error(err);
    }
  } else {
    console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
  }
});
