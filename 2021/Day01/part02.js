const lib_func = require('../lib/functions.js');

data_array = lib_func.load_input_in_array('input.txt')
data_array = data_array.map((x) => parseInt(x, 10))

const counter = data_array.reduce((count, value, index, array) => {
  const sum_a = array.slice(index, index + 3).reduce(
    (total, num) => total + num, 0);
  const sum_b = array.slice(index + 1, index + 4).reduce(
    (total, num) => total + num, 0);

  if (sum_a < sum_b) {
    return count += 1
  } else {
    return count
  }
}, 0);

console.log("Part 02 - Solution : ", counter)