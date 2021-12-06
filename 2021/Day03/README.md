## Advent of Code 2021 - Day 03 Part 01

### Puzzle
The puzzle is described here :  
https://adventofcode.com/2021/day/3

### Prerequisites
- node.js installed

### How to Run
- git clone the repo 
- ```$ cd Advent_Of_Code/2021/Day03/```
- Run the code in a terminal with the command ```$ node part01.js```

### Thoughts while doing Part 01
- In function "calculate_rate" I iterate through all the bits of every element of the input data. 
- I save all the bits from each position in an array (with the help of the ```map``` method).
- Then in this array (of all the bits from the same position) I use the ```reduce``` method 
and I create a js object with how many zeros and how many ones I have.

Inspired to use the ```reduce``` method from this article again 
https://www.freecodecamp.org/news/reduce-f47a7da511a9/ 
(example of tally)
- The one that is bigger (depending on what I want -gamma or epsilon rate-) I add it to my resulting string.

### Solution
- Correct Answer (based on the given input) : 1092896

![Aoc Part 01 - Day 3 - 2021](https://github.com/Imod7/Advent_Of_Code/tree/master/images/2021/day03_part01.png "Aoc Part 01 - Day 3 - 2021")
