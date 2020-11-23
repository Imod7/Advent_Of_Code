# AoC 2018

## Day 1 - Part 2

The subject of the problem is described here 
https://adventofcode.com/2018/day/1

### **The problem**
So in this part I have to add up (I start from 0) every number from the input file and check if after every addition I have the same result twice. If I do, the program stops and I give back the result.

### **First solution**
So what I thought was to read the input numbers, add them up and save every result in a dictionary. The indexes of my dictionary are my results and the values of the dictionary are how many times I have seen this result. If I dont find the same result on the first run of the input, I need to run again and again the input file using as the starting point not zero but the result from the last run.

### **Got stuck**
I got stuck a little bit on this one because it was taking forever the program to finish. I thought the cause was that my code had to be more efficient but the real reason was that my code had a BUG. Due to this error, I made my code run faster but it took some time.

### **Where are you, miss Pattern ?**
So first I tried to find patterns on my results after the multiple runs. I was checking the results after each run and I saw that they were all multiples of the first run which was 543. So in the second round my result was 1086 (= 543 * 2), in the third round it was 1629 (= 543 * 3), fourth 2172 and so on... Ok thats a good pattern but doesnt solve my issue...

### **Where are you, miss Pattern no2 ?**
Then I checked the input file. I opened the input and I saw it has different numbers and at the end it has the number +75248. I tried to run the program with smaller input files (i deleted some numbers from the end) and it was running instantly and giving the solution. Then I run for more numbers and more and more. What I noticed was that the program was running instantly if I just deleted the last number from the input file, the +75248. So I thought that it has something to do with this number. While I was trying to figure out a pattern compared to that number, I remembered another problem I had in codewars and Emily (emiflake in github) pointed out the modulo. And with modulo you actually go into circles, I mean based on your modulo you go back to your starting range.

### **We go higher and higher**
So until the number 75248, my results kept increasing so the probability I am gonna have the same sum/result is very little to none. So maybe with the number 75248 I make a full circle which means after that I go back to my initial range of numbers. In this initial range it would be the most probable also to find a result same as I already have in my dictionary. Hence, find the solution since the goal is to find a duplicate result.

### **Going into circles and TaaaDaaaa !!!**
So I checked how many times 543 goes into my big number 75248 and it goes 138 times (75248 / 543 = 138.578). So maybe after 138 rounds I will go back to the initial range I was in the start where its most probable to find the duplicate. So why run all the 138 rounds and not just go directly to that round. I just need to run the first round by giving initial frequency 0 and get the first results in my dictionary. Then skip all the 138 rounds, calculate directly the frequency after 138 rounds which is 138 * 543 = 74934 (since in all the rounds the resulting frequency is multiple of 543) and run only a second round by giving directly the frequency 74934. And yes, the solution/duplicate was found in that round and the program stopped and gave the solution.

### **Lesson Learned**
You think you are solving an issue (making your code more efficient) whilst you are solving another one (your code is just buggy and you are trying to fix it) and in the meantime you are playing the pattern-hunterer game, refreshing your maths and actually having loads of fun by yourself. :)