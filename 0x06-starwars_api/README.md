# Star Wars API

## Description
This project contains a script that interacts with the Star Wars API (SWAPI) to retrieve and display character information from Star Wars movies. The script takes a movie ID as input and prints all character names that appear in that movie.

## Requirements
- Ubuntu 20.04 LTS
- Node.js 10.14.x
- Request module
- Semistandard style

## Installation

1. Install Node.js 10:
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2. Install semistandard:
```bash
sudo npm install semistandard --global
```

3. Install request module:
```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Usage
```bash
./0-starwars_characters.js [movie_id]
```

Example:
```bash
./0-starwars_characters.js 3
```

## Files
- `0-starwars_characters.js`: Main script that fetches and displays Star Wars character names

## Features
- Fetches character data from the Star Wars API
- Displays character names in the order they appear in the movie's character list
- Handles errors gracefully
- Follows semistandard JavaScript style

## Author
ALX Software Engineering Programme