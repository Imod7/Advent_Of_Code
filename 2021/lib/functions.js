const fs = require('fs')

/**
 * Reads a text file, takes every line and saves it as an element in an array.
 * @return {Array} Returns an array of strings (lines in file).
 */
function load_input_in_array(filename) {
  try {
      const input_data = fs.readFileSync(filename, 'utf-8')
      return input_data.split('\n')
  } catch (err) {
      console.log(err)
  }
}

module.exports = { load_input_in_array }
