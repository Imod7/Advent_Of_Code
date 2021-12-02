const lib_func = require('../lib/functions.js');
const colors = require('../lib/colors.js');

var data_array = lib_func.load_input_in_array('input.txt');

function move_calculation(move_str, data_array) {
  var move_result = data_array.map(function(str) {
    var regex_pattern = new RegExp('(?<=' + move_str + ' ).*');
    res = str.match(regex_pattern);
    return (res ? +res[0] : +res);
  }).reduce((total, amount) => total + amount);
  return move_result;
}

const forward_total = move_calculation("forward", data_array);
const down_total = move_calculation("down", data_array);
const up_total = move_calculation("up", data_array);
const depth = down_total - up_total

console.log("Total of forward / horizontal moves : ", forward_total);
console.log("Total of down moves : ", down_total);
console.log("Total of up moves : ", up_total);
console.log("Total of depth: ", down_total - up_total);
console.log();
console.log(FgGreen, "Part 01 Solution [ Horizontal * Depth ] : ", forward_total * depth);
