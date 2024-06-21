words = input(">")
vowels = "aeiou"
final_word = 0

for i in words:
    if i in vowels:
       final_word += 1


print(final_word)