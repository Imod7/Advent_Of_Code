const lib_func = require('../lib/functions.js');
const colors = require('../lib/colors.js');

var data_array = lib_func.load_input_in_array('input copy.txt');

function move_calculation(move_str, data_array) {
  var move_result = data_array.map(function(str) {
    var regex_pattern = new RegExp('(?<=' + move_str + ' ).*');
    res = str.match(regex_pattern);
    return (res ? +res[0] : +res);
  }).reduce((total, amount) => total + amount);
  return move_result;
}

function create_move_array(move_str, data_array) {
  var move_result = data_array.map(function(str) {
    var regex_pattern = new RegExp('(?<=' + move_str + ' ).*');
    res = str.match(regex_pattern);
    // console.log(res);
    return (res ? +res[0] : +res);
  });
  return move_result;
}

const forward_total = move_calculation("forward", data_array);

const forward_array = create_move_array("forward", data_array);
const up_array = create_move_array("up", data_array);
const down_array = create_move_array("down", data_array);


var up_down = down_array.map(function (num, idx) {
  return num - up_array[idx];
}); 

// var depth = 0;
// var aim = 0;

// for (let i = 0; i < up_down.length; i++) {
//   if (forward_array[i]) {
//     depth += forward_array[i] * aim;
//   } else {
//     aim += up_down[i];
//   }
// }

var sum_aim = forward_array.map(function (num, idx) {
  const aim = up_down.slice(0, idx + 1).reduce(function(total, amount){
    return total + amount
  }, 0); 
  return num * aim
}); 

const depth = sum_aim.reduce((total, amount) => total + amount); 

// console.log("Total of forward / horizontal moves : ", forward_total);
// console.log("Total of down moves : ", down_total);
// console.log("Total of up moves : ", up_total);
// console.log("Total of depth: ", new_depth);
console.log();
console.log(FgGreen, "Part 02 Solution [ Horizontal * Depth ] : ", forward_total * depth);
