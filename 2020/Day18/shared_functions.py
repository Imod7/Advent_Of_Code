from typing import Dict, List, Text

def get_file_lines(file_name='input.txt') -> List[Text]:
    """Function that opens and reads the input text file line by line.

    :param file_name: If no parameter is given it reads by default the input.txt file.
    :return: a list of strings. Each string is a line read from the input file.
    """
    input_file = open(file_name, "r")
    file_lines = input_file.readlines()
    return file_lines