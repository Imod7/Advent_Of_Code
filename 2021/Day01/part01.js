const lib_func = require('../lib/functions.js');

data_array = lib_func.load_input_in_array('input.txt')

const counter = data_array.reduce((count, value, index, array) => {
  if ((index > 0) && (parseInt(value) > parseInt(array[index - 1]))) {
    return count += 1
  } else {
    return count
  }
}, 0);

console.log("Part 01 - Solution : ", counter)
