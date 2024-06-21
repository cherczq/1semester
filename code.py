products = ["lemons", "tomatoes", "coconut", "rice", "apples"]
products2 = list()

print("products in stock:")
number = 1
for product in products:
    print(number, product)
    number += 1

print("supply of products")
print("enter the product name or “exit” to exit")
while True:
    product = input(":")

    if product == "exit":
        break
    else:
      products.append(product)

print("products in stock")
number = 1
for product in products:
    print(number, product)
    number += 1
print("Enter the number of the product you want to buy")
product_index = int(input(":"))
if 0 <= product_index < len(products):
    product = products.pop(product_index)
    products2.append(product)
    print("You purchased", product)
    print("Thenk you for your purchase")
else:
    print("Wrong number")

print("Products at the end of the day:")
number = 1
for product in products:
    print(number, product)
    number += 1

print("Products sold per day:")
products2.reverse()

for product in products2:
    print(product)

