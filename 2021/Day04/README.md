### Advent of Code 2021 - Day 04 Part 01

#### Puzzle
The puzzle is described here :  
https://adventofcode.com/2021/day/4

#### Prerequisites
- node.js installed

#### How to Run
- git clone the repo 
- ```$ cd Advent_Of_Code/2021/Day03/```
- Run the code in a terminal with the command ```$ node part01.js```

#### Solution part01
- Correct Answer (based on the given input) : 29440

#### Save the data (& yourself! :P)
So how to best store the input data so we can then access what we need in an efficient way (fast & easy). 
  * I saved every board in an array (all rows and columns in one (flattened) array of 25 elements `array_boards`)
  * For every board / array I also created a dictionary (`board_dicts`) with key the number element and value a string that it is a concatenation of :
    * a flag that indicates if the number was marked (1) or not (0) _When I save a number for the first time it has flag = 0_  +
    * the index of the element in the board.
    So the value in the dictionary of a number that it is in position 12 in the board would be "012".

#### Iterate & Check
  * For every number in the caller array (array that contains all the numbers that were drawn) I check against every board.
  * If the number exists in a board then :
      1) I change its flag from 0 to 1 (in `board_dicts`).
      2) Check if its row or column is a winning one. This check is done by getting all the elements in the same row and check their flag (from the dictionary). The same check is done for the column.
      3) As soon as I find a row or column that all its elements have their flag equal to 1, I call Bingo and calculate the sum (of items that have flag 0).
      4) Then I calculate also the product with the drawn number and give this as the solution to the puzzle.

  *** To check the winning row or column I use the index of the number in the board and with `modulo` I extrapolate the row and column 

#### Thoughts while doing Part 01
* When using a dictionary, the time to access/retrieve an element is very fast ( O(1) ). So by saving the elements of the board also in a dictionary, I can see very fast if a number/key exists in this board without doing any iteration (as I would do if I used an array).
* The downside of the dictionary is that I do not know the order/position of the elements in the board. That is why I save "flag + index" of the element as its value in the dictionary. Since I know the index I can directly check the element's row and column without iterating the whole array.


#### Solution part02
- Correct Answer (based on the given input) : 13884

#### Thoughts while doing Part 02
* One thing to pay attention was once a board was a winning board then I should not change it again so exclude it from the check / updates. 
* Also, very handy to save the index of a winning board in a `Set` object so I have another layer of safety that I do not save duplicates. Also, `sets` keep the insertion order so I know that the last element of the set `bingo_boards` is the last winning board.
* Last, I had to save the number that was drawn when the last board won so I did that by just changing the bingo function from part01 and passing  there the number drawn as an argument and recalculating every time the sum and solution.
* The solution is the last bingo calculation.
