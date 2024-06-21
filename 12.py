first_name = 'Anna'
last_name = 'Cherkashyna'
gender = 'woman'
is_woman = gender == 'woman'
print(gender, type(gender))
print(is_woman, type(is_woman))

if is_woman:
    sex = "ledi"
else:
    sex = "mr"
grettings = f"Hello, {sex} {first_name} {last_name}!"
print(grettings)