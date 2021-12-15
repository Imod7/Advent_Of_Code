const lib_func = require('../lib/functions.js');

const input_data = lib_func.load_input_in_array('input.txt');

console.log(input_data);

const caller_nums = input_data[0].split(",");
const boards = input_data.slice(1);

// Save the data of the boards in an array of arrays of arrays
var array_boards = [];
j = 0;
for (var i = 0; i < boards.length; i++) {
  if (j % 6 == 0) {
    var arr_board = [];
    array_boards.push(arr_board);
  }
  if (boards[i] != "") {
    var array_row = boards[i].split(" ");
    arr_board.push(array_row.filter(elem => elem != ""));
  }
  j += 1;
}

console.log("array boards : ", array_boards);

console.log("Number of boards : ", array_boards.length);

console.log("caller_nums : ", caller_nums);

