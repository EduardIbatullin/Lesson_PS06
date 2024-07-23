#
data = [
    [100, 110, 120],
    [400, 500, 600],
    [150, 140, 130]
    ]


list = []


for row in data:
    for item in row:
        if item > 130:
            list.append(item)

print(list)

