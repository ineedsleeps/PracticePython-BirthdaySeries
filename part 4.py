import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


def gen_counts():
    with open("birthday.json", "r") as f:
        birthdays = json.load(f)
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
    print(months)
    counter = Counter(months)
    return counter

def gen_graph(count):
    x_cat = []
    x = []
    y = []
    for key, value in count.items():
        x.append(key)
        y.append(value)
    print(x)
    print(y)
    p=figure(x_range=x)
    p.vbar(x=x, top=y, width=0.5)
    show(p)

def main():
    gen_graph(gen_counts())

if __name__ == '__main__':
    main()