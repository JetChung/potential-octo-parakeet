import parse

(names, weights, costs) = parse.get_data();
weight = 0
price = 0
items = []
while (weight < 200):
    item = max(costs, key=costs.get)
    items.append(item)
    weight += weights[item]
    price += costs[item]
    costs[item] = 0;

price -= costs[items[-1]]
weight -= weights[items[-1]]
print("price: " + str(price) +  ", weight: " + str(weight))
# gives price: 3431.88, weight: 198.06