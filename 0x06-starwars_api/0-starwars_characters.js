#!/usr/bin/node
const request = require('request');
const util = require('util');

// Convert request to promise-based
const requestAsync = util.promisify(request);

// Base URL for Star Wars API
const BASE_URL = 'https://swapi.dev/api';

// Function to get character name from URL
async function getCharacterName (url) {
  try {
    const response = await requestAsync(url);
    const character = JSON.parse(response.body);
    return character.name;
  } catch (error) {
    console.error(`Error fetching character: ${error}`);
    return null;
  }
}

// Main function to get all characters from a movie
async function getMovieCharacters (movieId) {
  try {
    // Get movie data
    const response = await requestAsync(`${BASE_URL}/films/${movieId}/`);
    const movie = JSON.parse(response.body);
    
    // Get all character names in order
    const characterPromises = movie.characters.map(url => getCharacterName(url));
    const names = await Promise.all(characterPromises);
    
    // Print character names
    names.forEach(name => {
      if (name) console.log(name);
    });
  } catch (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }
}

// Get movie ID from command line arguments
const movieId = process.argv[2];

// Validate movie ID
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

// Execute main function
getMovieCharacters(movieId);