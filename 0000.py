
tasks = []
caunt = 0
print("Введіть ваші завдання на сьогодні. Введіть 'q' для завершення.")

while True:
    task = input("Введіть завдання: ")
    if task == 'q':
        break
    tasks.append(task)

print("Ваші завдання на сьогодні:", task)
for i in tasks:
    caunt += 1
    print(caunt,i)
