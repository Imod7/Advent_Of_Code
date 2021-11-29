const colors = require('./colors');
const fs = require('fs')

var acc = 0

function execute_instruction(lines_array, cur_index) {
    var inst = lines_array[cur_index]
    var inst_num = parseInt(inst.substr(4))
    let action = inst.substr(0, 3)

    if (action == 'jmp') {
        cur_index = parseInt(cur_index) + inst_num
    } else if (action == 'acc') {
        acc += inst_num
        cur_index += 1
    } else {
        cur_index += 1
    }
    return cur_index
}

function debugging_print(index, lines_array, cur_index, indexes_checked) {
    if (index == 0) {
        console.log(FgGreen, "Before the execution of the instruction :", FgYellow, lines_array[cur_index])
        console.log(FgGreen, "Visited indexes", Reset)
        console.log(indexes_checked.slice(-90).join(' '))
        console.log(FgGreen, "Current index :", cur_index)
        console.log(FgGreen, "Value of accumulator :", acc)
    } else {
        console.log(FgMagenta, "After the execution of the instruction")
        console.log(FgMagenta, "New index", cur_index)
        console.log(FgMagenta, "New index exists? ", indexes_checked.indexOf(cur_index))
        console.log(FgMagenta, "Value of accumulator: ", acc)
    }
}

fs.readFile('input.txt', 'utf-8', (err, data) => {
    var indexes_checked = [0]
    if (err) {
        console.error(err)
        return
    }
    let lines_array = data.split("\n")
    cur_index = lines_array.indexOf(lines_array[0])
    while (1) {
        console.log()
        debugging_print(0, lines_array, cur_index, indexes_checked)
        var cur_index = execute_instruction(lines_array, cur_index)
        debugging_print(1, lines_array, cur_index, indexes_checked)
        if (indexes_checked.indexOf(cur_index) != -1)
            break
        indexes_checked.push(parseInt(cur_index))
        indexes_checked.sort()
    }
    console.log()
    console.log(FgCyan, "Final value of accumulator: ", acc)
});
