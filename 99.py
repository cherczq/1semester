#Напишіть програму, яка знаходить максимальний елемент у списку.
numbers = [6,8,3]
max = 0
for i in numbers:
    if i >= max:
        max = i
print(max)