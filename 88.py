
power = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
sum = 0
mid = 0
for i in power:
    sum = sum + i
mid = sum / len(power)
print(f"{mid} \n" f"{len(power)}")


