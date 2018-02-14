import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


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
