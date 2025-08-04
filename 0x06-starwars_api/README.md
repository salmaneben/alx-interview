# 0x06. Star Wars API

## 📝 Description

This project creates a script that interacts with the Star Wars API (SWAPI) to retrieve and display character information from Star Wars movies. The script demonstrates asynchronous programming, API consumption, and data manipulation in Node.js.

The challenge focuses on making HTTP requests, handling promises, and processing JSON data from external APIs.

## 🎯 Learning Objectives

- Master asynchronous programming with callbacks and promises
- Learn to consume REST APIs and handle HTTP requests
- Practice error handling in asynchronous operations
- Understand JSON data parsing and manipulation
- Work with Node.js and external modules

## 📋 Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS
- Node.js version 10.14.x
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- Code should follow semistandard style
- All files must be executable
- Use of `request` module for HTTP requests

## 🚀 Implementation

### Script Purpose
```javascript
// Fetch and display all character names from a Star Wars movie
// Usage: ./0-starwars_characters.js <movie_id>
```

### API Endpoint
```
Base URL: https://swapi.dev/api/
Movies: https://swapi.dev/api/films/{movie_id}/
Characters: Individual character URLs from movie response
```

## 📁 Files

| File | Description |
|------|-------------|
| `0-starwars_characters.js` | Main script for fetching Star Wars character data |
| `README.md` | Project documentation and usage guide |

## ⚙️ Installation

### 1. Install Node.js 10
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 2. Install Required Modules
```bash
# Install request module globally
sudo npm install request --global

# Set NODE_PATH for global modules
export NODE_PATH=/usr/lib/node_modules

# Install semistandard for code style
sudo npm install semistandard --global
```

### 3. Verify Installation
```bash
node --version    # Should show v10.x.x
npm --version     # Should show compatible version
```

## 🧪 Usage

### Basic Usage
```bash
# Make script executable
chmod +x 0-starwars_characters.js

# Run with movie ID
./0-starwars_characters.js 3
```

### Movie ID Reference
| Movie ID | Movie Title |
|----------|-------------|
| 1 | A New Hope |
| 2 | The Empire Strikes Back |
| 3 | Return of the Jedi |
| 4 | The Phantom Menace |
| 5 | Attack of the Clones |
| 6 | Revenge of the Sith |

### Expected Output Example
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## 🔍 Algorithm Explanation

### Step-by-Step Process:

1. **Parse Input**: Get movie ID from command line arguments
2. **Fetch Movie Data**: Make HTTP request to get movie information
3. **Extract Characters**: Get character URLs from movie response
4. **Fetch Character Data**: Make requests for each character URL
5. **Display Results**: Print character names in correct order

### Key Challenges:
- **Asynchronous Operations**: Managing multiple HTTP requests
- **Order Preservation**: Maintaining character order from API
- **Error Handling**: Graceful handling of network failures

## 💻 Code Structure

### Main Components:

```javascript
// 1. HTTP Request Setup
const request = require('request');

// 2. Movie Data Fetching
request(movieUrl, function(error, response, body) {
    // Handle movie response
});

// 3. Character Data Processing
// Using async/await or Promise.all for concurrent requests

// 4. Sequential Output
// Ensuring characters print in correct order
```

### Asynchronous Patterns Used:

1. **Callback-based**: Traditional Node.js pattern
2. **Promise-based**: Modern async handling
3. **Async/Await**: Cleaner asynchronous code

## 🔍 Technical Details

### HTTP Requests
```javascript
// Basic request structure
request(url, function(error, response, body) {
    if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        // Process data
    } else {
        console.error('Error:', error);
    }
});
```

### Error Handling
- Network connectivity issues
- Invalid movie IDs
- API response errors
- JSON parsing errors

### Performance Considerations
- Concurrent character requests for better performance
- Proper error handling to avoid crashes
- Memory management for large datasets

## ✅ Testing

### Test Different Movies
```bash
# Test various movie IDs
./0-starwars_characters.js 1  # A New Hope
./0-starwars_characters.js 2  # The Empire Strikes Back
./0-starwars_characters.js 6  # Revenge of the Sith
```

### Error Testing
```bash
# Test error cases
./0-starwars_characters.js 999  # Invalid movie ID
./0-starwars_characters.js      # No arguments
```

### Code Style Check
```bash
# Check code style with semistandard
semistandard 0-starwars_characters.js
```

## 🚨 Common Issues

1. **Module Not Found**: Ensure request module is installed globally
2. **Permission Denied**: Make script executable with `chmod +x`
3. **API Timeouts**: Handle network errors appropriately
4. **Node Version**: Ensure Node.js 10.x is installed

## 🔗 Related Concepts

- **REST APIs**: Understanding RESTful web services
- **HTTP Methods**: GET requests and response handling
- **JSON Processing**: Parsing and manipulating JSON data
- **Asynchronous Programming**: Callbacks, Promises, Async/Await
- **Error Handling**: Graceful failure management

## 📚 Resources

- [Star Wars API (SWAPI) Documentation](https://swapi.dev/documentation)
- [Node.js Request Module](https://www.npmjs.com/package/request)
- [JavaScript Async Programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- [Node.js Official Documentation](https://nodejs.org/en/docs/)
- [Semistandard Style Guide](https://github.com/standard/semistandard)

## 🎬 API Reference

### Movie Endpoint
```
GET https://swapi.dev/api/films/{id}/
```

### Character Endpoint
```
GET https://swapi.dev/api/people/{id}/
```

### Response Structure
```json
{
  "title": "Return of the Jedi",
  "characters": [
    "https://swapi.dev/api/people/1/",
    "https://swapi.dev/api/people/2/",
    // ... more character URLs
  ]
}
```