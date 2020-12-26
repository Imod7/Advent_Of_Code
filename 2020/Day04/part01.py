from typing import Dict, List, Text


class Passport:
    """Class Passport to store the input data per batch/object."""

    def __init__(self, batch_data: Dict[Text, Text]):
        """Setting all the passport fields/object's attributes from dictionary batch_data"""
        self.valid = False
        self.ecl = None
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        for key in batch_data:
            setattr(self, key, batch_data[key])

    def check_missing_fields(self):
        """Checking if the passport object is valid"""
        if self.ecl is None:
            pass
        elif self.byr is None:
            pass
        elif self.iyr is None:
            pass
        elif self.eyr is None:
            pass
        elif self.hgt is None:
            pass
        elif self.hcl is None:
            pass
        elif self.ecl is None:
            pass
        elif self.pid is None:
            pass
        else:
            self.valid = True


def get_file_lines(file_name='input.txt') -> List[Text]:
    """Function that opens and reads the input text file line by line.
    
    :param file_name: If no parameter is given it reads by default the input.txt file.
    :return: a list of strings. Each string is a line read from the input file.
    """
    input_file = open(file_name, "r")
    file_lines = input_file.readlines()
    return file_lines


def split_data(batch: Text) -> Dict[Text, Text]:
    batch = batch.rstrip()
    y = [x.rstrip() for x in batch.split(" ")]
    # print(y)
    z = [x.split(":") for x in y]
    # print(z)
    # try:
    z = dict([x.split(':') for x in y])
    # except:
    #     print("ERROR")
    #     pass
    # print("final:", z)
    return z


def list_of_batches(input_data) -> List[Dict[Text, Text]]:
    batch = ""
    batch_list = {}
    all_batches = []
    for lines in input_data:
        if lines != "\n":
            batch = batch + lines.strip() + " "
        else:
            batch_list = split_data(batch)
            all_batches.append(batch_list)
            batch = ""
    batch_list = split_data(batch)
    all_batches.append(batch_list)
    # print(all_batches)
    return all_batches


def main() -> None:
    input_data = get_file_lines()
    all_batches = list_of_batches(input_data)
    valid_objects = 0
    for batch in all_batches:
        # for key, value in batch.items():
        #     print(key, " ", value)
        obj = Passport(batch)
        obj.check_missing_fields()
        if obj.valid is True:
            valid_objects += 1
    print("Amount of valid passports : ", valid_objects)


if __name__ == "__main__":
    main()
