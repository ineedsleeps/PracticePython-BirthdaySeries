
if __name__ == '__main__':

    birthday_dict = {
        'Colby': '05/25/1991',
        'Tiffany': "09/27/1990",
        'Albert': '03/14/1879',
        'Rowan': '01/006/1955'
        }
    print('Welcome to the birthday dictionary.')
    print('We know the birthdays of: ')
    for name in birthday_dict:
        print(name)

    name = input('Who\'s birthday would you like to look up? ')
    if name in birthday_dict:
        print("{}\'s birthday is {}.".format(name, birthday_dict[name]))
    else:
        print("We don't have that birthday in the dictionary. ")
