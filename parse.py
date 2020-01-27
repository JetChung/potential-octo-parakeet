with open("data.csv", "r") as f:
    data = f.read();
    list = data.split(" ")
dict = {}
while (len(list) > 0):
    dict[list[0]] = [list[1], list[2]]
    print(len(list))
    list.pop(0)
    print(len(list))
    list.pop(1)
    print(len(list))
    list.pop(2)
print(dict)
