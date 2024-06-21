line = input("enter your line: ")

first_letter= line[0]

letter = 0

for i in line:
        if i == first_letter:
                  letter += 1

print("first letter written:", letter)