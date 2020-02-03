import re
import numpy as np


def get_data():
    weights, costs = np.zeros(100), np.zeros(100)

    with open("data.csv", "r") as f:
        data = f.read();
        list = re.split("\n", data)

    for i,k in enumerate(list):
        if len(list[i].split(" ")) > 1:
            weights[i] = (float(list[i].split(" ")[1]))

    for i,k in enumerate(list):
        if len(list[i].split(" ")) > 1:
            costs[i] = (float(list[i].split(" ")[2]))
    return (weights, costs)

weights, costs = get_data()

class pack:
   def __init__(self, items):
       self.items = items
       
   def get_weight(self):
       return (np.dot(items, weights))
   def get_cost(self):
        return np.dot(items, costs)

   def is_valid(self):
        return (np.dot(items, weights) < 200)
items = np.ones(100)
a = pack(items)
print(a.is_valid())

start with 1000