import re

def get_data():
    names, weights, costs = {}, {}, {}

    with open("data.csv", "r") as f:
        data = f.read();
        list = re.split("\n", data)

    for i,k in enumerate(list):
        if len(list[i].split(" ")) > 1:
            names[i] = list[i].split(" ")[0]

    for i,k in enumerate(list):
        if len(list[i].split(" ")) > 1:
            weights[i] = float(list[i].split(" ")[1])

    for i,k in enumerate(list):
        if len(list[i].split(" ")) > 1:
            costs[i] = float(list[i].split(" ")[2])
    return (names, weights, costs)