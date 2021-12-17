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

function check_if_winning_col(j, index) {
  for (var i = 0; i < 5; i++) { 
    if (board_dicts[j][array_boards[j][(index % 5) + (i * 5)]][0] == "0") {
      return 0;
    }
  }
  return 1;
}

function check_if_winning_row(j, index) {
  for (var i = 0; i < 5; i++) { 
    if (board_dicts[j][array_boards[j][index - (index % 5) + i]][0] == "0") {
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

const bingo_boards = new Set()

function bingo(j, last_draw) {
  console.log("Number drawn : ", last_draw)
  var sum = calculate_sum(j);
  console.log("Sum : ", sum)
  console.log(FgGreen, Bright, "****BINGO****", Reset);
  console.log(BgMagenta, FgGreen, Bright, "Solution (sum * num) = ", sum * parseInt(last_draw), Reset);
}

for (var i = 0; i < caller_nums.length; i++) {
  for (var j = 0; j < board_dicts.length; j++) {
    if (caller_nums[i] in board_dicts[j]) {
      if (!(bingo_boards.has(j))) {
        board_dicts[j][caller_nums[i]] = "1" + board_dicts[j][caller_nums[i]].slice(1);
        if ((check_if_winning_row(j, parseInt(board_dicts[j][caller_nums[i]].slice(1))) == 1) ||
          (check_if_winning_col(j, parseInt(board_dicts[j][caller_nums[i]].slice(1))) == 1)) {
          bingo_boards.add(j);
          bingo(j, caller_nums[i]);
        }
      }
    }
  }
}
