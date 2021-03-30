def fizz_buzz():
    # your code here
    for i in range(1,101):
       if i % 3 == 0 and i % 5 != 0:
           number = "Fizz"
       elif i % 5 == 0 and i % 3 != 0:
           number = "Buzz"
       elif i % 3 == 0 and i % 5 == 0:
           number = "FizzBuzz"
       else:
           number = i
       print(number)
    return number

fizz_buzz()