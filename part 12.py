import json
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
    person = input("Please input the name: ")
    date = input("Please input the birthday (MM/DD/YYYY): ")
    birthdays[name] = date
    with open("birthday.json", "w") as f:
        json.dump(birthdays, f)


if __name__ == '__main__':
    birthdays = read_dict()
    print('Welcome to the birthday dictionary.')
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
