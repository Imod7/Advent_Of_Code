## Advent of Code 2021 - Day 04 Part 01

### Puzzle
The puzzle is described here :  
https://adventofcode.com/2021/day/4

### Prerequisites
- node.js installed

### How to Run
- git clone the repo 
- ```$ cd Advent_Of_Code/2021/Day03/```
- Run the code in a terminal with the command ```$ node part01.js```

### Solution
- Correct Answer (based on the given input) : 

### Thoughts while doing Part 01

#### Save the data (& yourself! :P)
So how to best store the input data so we can then access what we need in an efficient way (fast & easy). 

I will try the following way :
  * First I save all the input in an array (`input_data`) with my generic function (`load_input_in_array`).
  * Then I take the first line which is the caller numbers and save it in the `caller_nums array` and the rest (from the element 1 onwards) in `boards`.
  * But maybe it is a good idea (idk, I am just testing) to save the boards as an array of arrays of arrays which will correspond to :
    * the outer array will be the wrapper of all the data (all boards and all rows of every board).
    * the first level inner array to indicate the corresponding board.
    * the second level inner array to indicate the corresponding row of every board.
  * **Note** : to save every board in a separate array I use my all time favourite **modulo**!

  #### Iterate & Check (LE winner!)
  Now I need to iterate and check. Not yer implemented but I will try to :
  * Take the first 5 numbers from `caller_nums`.
  * Go through all the boards.
  * In every board check every row against the `caller_nums`.

  _To Be Continued! Sooon!!!_