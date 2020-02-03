import parse

(names, weights, costs) = parse.get_data()

ratio = {}
for i in range(0,100):
    ratio[i] = float(costs[i])/float(weights[i])
    
weight = 0
price = 0
items = []
while (weight < 200):
    item = max(ratio, key=ratio.get)
    items.append(item)
    weight += weights[item]
    price += costs[item]
    costs[item] = 0;
    ratio[item] = 0;

price -= costs[items[-1]]
weight -= weights[items[-1]]
print("price: " + str(price) +  ", weight: " + str(weight))
# improvement on naive greedy
# price: 3940.0, weight: 199.33