#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let characters = [];
const names = [];

// Function to fetch movie characters
const requestCharacters = async () => {
  await new Promise((resolve, reject) => request(filmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      reject(new Error(`Error: ${err} | StatusCode: ${res?.statusCode}`));
    } else {
      const jsonBody = JSON.parse(body);
      characters = jsonBody.characters;
      resolve();
    }
  }));
};

// Function to fetch character names
const requestNames = async () => {
  if (characters.length > 0) {
    for (const character of characters) {
      await new Promise((resolve, reject) => request(character, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          reject(new Error(`Error: ${err} | StatusCode: ${res?.statusCode}`));
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    throw new Error('Error: No characters found');
  }
};

// Main function to get and print character names
const getCharNames = async () => {
  try {
    await requestCharacters();
    await requestNames();

    names.forEach((name, index) => {
      if (index === names.length - 1) {
        process.stdout.write(name);
      } else {
        process.stdout.write(name + '\n');
      }
    });
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
};

// Execute the main function
getCharNames();