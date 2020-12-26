# Day 04 - Part 01

## Ideas for structures to implement
I solved Part 01 of Day 04 with the help of a class and not with plain dictionaries or lists just to practice with Python OOP. So I create an object of the class Passport for each batch of input data. 
However, I don't know how the use of classes and objects affects the memory efficiency. Searching about efficiency, I found this stackoverflow post [Dictionary vs Object - which is more efficient and why?](https://stackoverflow.com/questions/1336791/dictionary-vs-object-which-is-more-efficient-and-why) that mentions __slots__ but haven't tried it yet.

## Steps to solve the problem
- I first open the file and read it line by line. This happens in function get_file_lines. So I have a list structure called "input_data" with all my data.
- Then in function "list_of_batches" I create one line/string for each batch and I save it to variable batch.
- Then when I have one line per batch (I am in function "list_of_batches") I call function "split_data" that splits the line/batch and creates a dictionary with key value pairs for all the fields and corresponding values of the passport.
- Whenever I return a dictionary with all the fields of a batch I append it to list "all_batches" so I have all the batches in a list (a list of dictionaries). This happens also in function "list_of_batches".
- Then (in function "main") for each dictionary/batch in my list "all_batches", I create an object of class Passport and I populate the corresponding properties.
- After I populate the properties, I call method check_validity to check if one of the available fields (except the cid) is not populated. If one is not populated then I set the object's property "valid" to False.
- Last I have a variable "valid_objects" that counts the valid objects and this number is my answer to Part 01.


## How to Run 
You can download the file ```part01.py``` and ```input.txt``` and run the code in a Terminal with the command :

> ```python3 part01.py```


### Correct answer for my input data : 264