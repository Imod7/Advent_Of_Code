const lib_func = require('../lib/functions.js');
const colors = require('../lib/colors.js');

const input_array = lib_func.load_input_in_array("input.txt");

function calculate_rate(a, b) {
  var rate = "";
  for (let i = 0; i < 12; i++) {
    const bit_array = input_array.map(str => str.charAt(i));
    const count = bit_array.reduce((counter, bits) => {
      counter[bits] = (counter[bits] || 0) + 1;
      return counter;
    }, {});
    console.log(count);
    rate += (count[a] > count[b]) ? '0' : '1';
    console.log(rate);
  }
  return rate;
}

console.log(FgCyan, "Creating the gamma rate", Reset);
const gamma_rate = calculate_rate('0', '1');
console.log(FgCyan, "Creating the epsilon rate", Reset);
const epsilon_rate = calculate_rate('1', '0');

console.log(FgCyan, "gamma_rate : ", Reset, gamma_rate);
console.log(FgCyan, "epsilon rate : ", Reset, epsilon_rate);

console.log(FgGreen, "Solution Part 01 : ", parseInt(gamma_rate, 2) * parseInt(epsilon_rate, 2));
