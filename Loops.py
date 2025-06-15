
# fruits = ["Apple", "Banana", "Peach"]
# for fruit in fruits:
#     print(fruit) # her bir meyveyi teker teker yazdırır
#     print(fruits)

# for number in range(1, 11, 2): #adım 2 olarak belirlendi yani 2 artarak ilerler
#     print(number)
# print("---------------------------")
# for number in range(1, 11):
#     print(number)

# -------------------------Fizz-Buzz Game----------------------
for number in range(1, 101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print ("Buzz")
  else:
    print(number)




