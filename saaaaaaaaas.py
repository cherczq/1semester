words = input("what word?")
new_words = ""
for w in words:
       if w.isdigit():
           continue

       new_words = new_words + w
print(new_words )