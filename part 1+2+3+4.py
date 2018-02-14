import json
import bokeh
from collections import Counter
##birthday_dict = {
##    'Colby': '05/25/1991',
##    'Tiffany': "09/27/1990",
##    'Albert': '03/14/1879',
##    'Rowan': '01/06/1955'
##}
##
##with open("birthday.json", "w") as f:
##    json.dump(birthday_dict, f)

def read_dict():
    with open("birthday.json", "r") as f:
        birthdays = json.load(f)
        return birthdays

def write_to_dict():
    birthdays = read_dict()
    person = input("Please input the name: ")
    date = input("Please input the birthday (MM/DD/YYYY): ")
    birthdays[person] = date
    with open("birthday.json", "w") as f:
        json.dump(birthdays, f)

def look_up():
    birthdays = read_dict()
    print('We know the birthdays of: ')
    for name in birthdays:
        print(name)
    name = input('Who\'s birthday would you like to look up? ')
    if name in birthdays:
        print("{}\'s birthday is {}.".format(name, birthdays[name]))
    else:
        print("We don't have that birthday in the dictionary. ")
        print("Please enter the Name and Birthday in the prompts.")
        write_to_dict()

def count_month():
    birthdays = read_dict()
    num_to_string = {
	    1: "January",
	    2: "February",
	    3: "March",
        4: "April",
	    5: "May",
	    6: "June",
	    7: "July",
	    8: "August",
	    9: "September",
	    10: "October",
	    11: "November",
	    12: "December"
    }
    months = []
    for name, birthday_string in birthdays.items():
	    month = int(birthday_string.split("/")[0])
	    months.append(num_to_string[month])
    return(Counter(months))

def graph_birthdays():
    data = count_month()


if __name__ == '__main__':
    print('Welcome to the birthday dictionary.')
    while True:
        prompt = input("What would you like to do? Search, Add, Count, or Quit?").capitalize()
        if prompt == "Search":
            look_up()
        elif prompt == "Add":
            write_to_dict()
        elif prompt == "Quit":
            break
        elif prompt =="Count":
            print("Let's count the number of birthdays entered per month.")
            print(count_month())
        else:
            print("Input not recognized. Please enter again.")


