"""Internet Population's Graph"""

import pandas as pd
import pygal

def main(choice):
    """Core function"""
    if choice == "Number of Internet users by type" or choice == "1":
        analytic(input(), "/Tab1.csv", "Number of Internet users by type", "Region", 1, 5)
    elif choice == "Internet's using location" or choice == "2":
        analytic(input(), "/Tab2.csv", "Internet's using location", "Internet's using location", 2, 4)
    elif choice == "Time period of Internet's access" or choice == "3":
        analytic(input(), "/Tab3.csv", "Time period of Internet's access", "Region", 2, 9)
    elif choice == "Internet activities" or choice == "4":
        analytic(input(), "/Tab4.csv", "Internet activities", "activity to use Internet", 2, 12)

def analytic(year, path, name, x_axis_labels, start_select, stop_select):
    """Analysis function"""
    data_frame = pd.read_csv("../usedata/" + year + path)
    line_chart = pygal.Bar()
    line_chart.title = name + " in " + year
    line_chart.x_labels = list(data_frame[x_axis_labels])
    column_list = list(data_frame.columns.values)[start_select:stop_select]
    for column in column_list:
        raw_data_list = list(data_frame[column])
        total_list = list(data_frame["Total"])
        percentage_list = list()
        for i in range(len(raw_data_list)):
            if total_list[i] == 0:
                total_list[i] = 1
            percentage_list.append((raw_data_list[i] / total_list[i]) * 100)
        line_chart.add(column, percentage_list)
    line_chart.render_to_file("bar_chart.svg")

main(input())
