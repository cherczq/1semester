surname = "Введіть своє прізвище тут"


letter_frequency = {}
for i in surname:
    if i in letter_frequency:
        letter_frequency[i] += 1
    else:
        letter_frequency[i] = 1
