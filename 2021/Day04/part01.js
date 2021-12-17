const lib_func = require('../lib/functions.js');
const colors = require('../lib/colors.js');

const input_data = lib_func.load_input_in_array('input.txt');

const caller_nums = input_data[0].split(",");
const boards = input_data.slice(1);

// Save the data of the boards in an array of arrays of arrays
var array_boards = [];
var board_dicts = [];
j = 0;
for (var i = 0; i < boards.length; i++) {
  if (j % 6 == 0 && i != 0) {
    var board_dict = arr_board.reduce(function(map, num) {
      map[num] = "0" + arr_board.indexOf(num);
      return map;
    }, {});
    board_dicts.push(board_dict);
  }
  if (j % 6 == 0) {
    var arr_board = [];
    array_boards.push(arr_board);
  }
  if (boards[i] != "") {
    var array_row = boards[i].split(" ");
    arr_board.push(...array_row.filter(elem => elem != ""));
  }
  j += 1;
}

// console.log("array boards : ", array_boards);

// console.log("Number of boards : ", array_boards.length);

console.log("caller_nums : ", caller_nums);

// console.log("board_dicts : ", board_dicts);




function check_if_winning_col(j, index) {
  console.log("check index : ", index);
  for (var i = 0; i < 5; i++) { 
    console.log("check col [", i,"][", parseInt(index / 5), "] = " , array_boards[j][(index % 5) + (i * 5)]);
    if (board_dicts[j][array_boards[j][(index % 5) + (i * 5)]][0] == "0") {
      console.log("flag is : ", board_dicts[j][array_boards[j][(index % 5) + (i * 5)]][0], board_dicts[j][array_boards[j][(index % 5) + (i * 5)]]);
      return 0;
    }
  }
  return 1;
}

function check_if_winning_row(j, index) {
  console.log("check index : ", index);
  for (var i = 0; i < 5; i++) { 
    console.log("check row [", parseInt(index / 5),"][", i, "] = " ,array_boards[j][index - (index % 5) + i]);
    if (board_dicts[j][array_boards[j][index - (index % 5) + i]][0] == "0") {
      console.log("flag = ", board_dicts[j][array_boards[j][index - (index % 5) + i]][0], " from ", board_dicts[j][array_boards[j][index - (index % 5) + i]]);
      return 0;
    }
  }
  return 1;
}

function calculate_sum(j) {
  var total = 0;
  for (const [key, value] of Object.entries(board_dicts[j])) {
    if (value[0] == "0") {
      total += parseInt(key);
    } 
  }
  return total;
}

function bingo(j) {
  var sum = calculate_sum(j);
  console.log(FgGreen, Bright, "****BINGO****", Reset);
  console.log(BgMagenta, FgGreen, Bright, "Solution (sum * num) = ", sum * parseInt(caller_nums[i]));
  process.exit();
}

for (var i = 0; i < caller_nums.length; i++) {
  for (var j = 0; j < board_dicts.length; j++) {
    if (caller_nums[i] in board_dicts[j]) {
      board_dicts[j][caller_nums[i]] = "1" + board_dicts[j][caller_nums[i]].slice(1);
      console.log("num ", caller_nums[i], " exists in board [ ", j, " ] : ", board_dicts[j]);
      console.log("flag + index : ", board_dicts[j][caller_nums[i]]);
      console.log("check board : ", array_boards[j]);
      console.log(" --- Check if Winning Row --- ");
      if (check_if_winning_row(j, parseInt(board_dicts[j][caller_nums[i]].slice(1))) == 1) {
        bingo(j);
      }
      console.log(" --- Check if Winning Column --- ");
      if (check_if_winning_col(j, parseInt(board_dicts[j][caller_nums[i]].slice(1))) == 1) {
        bingo(j);
      }
    }
    
  }
}