## Advent of Code 2021 - Day 02 Part 01

### Puzzle
The puzzle is described here :  
https://adventofcode.com/2021/day/2

### Prerequisites
- node.js installed

### How to Run
- You can download the files from the current folder and
- Run the code in a terminal with the command ```$ node part01.js```

### Solution
- Correct Answer (based on the given input) : 2117664

### Thoughts while doing Part 01
- I was looking on how to combine filter and regex in order to make an array of only the elements that contain the word forward so I found this really cool & clean stackoverflow post
https://stackoverflow.com/questions/54321393/filter-array-containing-only-specific-word

- After having the array with only the elements that contain the word ```forward```, I would like to chnage my regex so I only extract the numbers next to the word ```forward```. For that I found this post : 
https://stackoverflow.com/questions/5006716/getting-the-text-that-follows-after-the-regex-match
that mentions the positive lookbehind assertion [wild stuff!]
This is explained in more detail here : 
https://www.regular-expressions.info/lookaround.html

- filter will just filter so I need to use a combination of fiter and map
- match the return is an object and I can access its elements. I can check that by printing 
```
var res = str.match(/(?<=forward ).*/)
console.log("result of match :", res);
so this will print 
result of match : [ '1', index: 8, input: 'forward 1', groups: undefined ]
```

in order to access to the properties of this object 
i can do 
```
console.log("result of match :", res);
    console.log("result of match :", res.input);
    console.log("result of match :", res[0]);
```

So I can use map
```
var horizontal = data_array.map(function(str) {
  var res = str.match(/(?<=forward ).*/)
  return (res ? +res[0] : +res)
});
```

and then add filter
```
var horizontal = data_array.map(function(str) {
  var res = str.match(/(?<=forward ).*/)
  return (res ? res[0] : res)
}).filter(str => str != null);
```

to remove the null elements

but if I convert the res directly into a number with '+res' then I will get zeros 
which does not affect my sum of the horizontal so 

```
var horizontal = data_array.map(function(str) {
  var res = str.match(/(?<=forward ).*/)
  return (res ? +res[0] : +res)
}).reduce((total, amount) => total + amount);
```

### Regex Change
To be able to use only one function I need to change the string forward and 
make it a variable but then I have to first save my regex pattern in a 
variable then convert to a regex object 
[found here 
https://stackoverflow.com/questions/25522595/convert-regex-string-to-regex-object-in-javascript
]
and change the pattern based on these 2 rules :
- You need to escape the backslash.
- You need to remove the forward slashes on the beginning and end of string.

### Resources 
Nice website to test regular expressions
https://regexr.com/6ao6a

### Thoughts while doing Part 02
The value of horizontal I have it from Part 01.
So I only need to calculate the depth which the multiplication 
of ```aim``` and ```forward```
but its multiplication of aim and forward based on their values 
every time we find a forward so maybe I need to 
1. create an array of aim where it has values only in the forward positions.
2. create an array of forwards with only values in the forward positions.

### Slice vs For loop
- The code where I slice and recalculate the ```aim``` is very ineffient but it was good practice to see the difference with a for loop. 

### Solution part 02
- Correct Answer on Part 02 (based on the given input) : 2073416724