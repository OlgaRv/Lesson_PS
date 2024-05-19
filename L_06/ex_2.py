# преобразование типа данных

data = [

    ['100', '110', '120'],
    ['400', '500', '600'],
    ['140', '160', '180']
]

numbers = []
for row in data:
    for text in row:
        number = int(text)
        numbers.append(number)

print(numbers)

# фильтрация данных

list = []
for row in data:
    for item in row:
        item = int(item)
        if item > 190:
            list.append(item)

print(list)