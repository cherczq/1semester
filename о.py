
first_list = []
second_list = []

while True:
    b = input("Enter a number (or 'stop' to complete): ")
    if b == "stop":
        break
    else:
        number = int(b)
        first_list.append(number)



for i in first_list:
    if i % 2 == 0:
        second_list.append(i)

print("First list:", first_list)
print("Sekond list:", second_list)