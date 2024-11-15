#!/usr/bin/node

const request = require('request');
const util = require('util');

// Convert request to use promises
const requestPromise = util.promisify(request);

// Base URL for the Star Wars API
const BASE_URL = 'https://swapi.dev/api';

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

async function getCharacterName(url) {
  try {
    const response = await requestPromise(url);
    const character = JSON.parse(response.body);
    return character.name;
  } catch (error) {
    console.error(`Error fetching character: ${error.message}`);
    return null;
  }
}

async function getMovieCharacters(movieId) {
  try {
    // Fetch movie data
    const response = await requestPromise(`${BASE_URL}/films/${movieId}/`);
    const movie = JSON.parse(response.body);
    
    // Get all character URLs from the movie
    const characterUrls = movie.characters;
    
    // Fetch all characters in parallel and maintain order
    const characterNames = await Promise.all(
      characterUrls.map(url => getCharacterName(url))
    );
    
    // Print character names, filtering out any null values from errors
    characterNames
      .filter(name => name !== null)
      .forEach(name => console.log(name));
    
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Execute the main function
getMovieCharacters(movieId);