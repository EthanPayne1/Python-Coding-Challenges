def fizzbuzz() -> None:

    n = int(input("Enter a number between 0-100: "))
    if n <= 100: 
        for i in range(n):
            if n % 5 == 0 and n % 3 == 0:
                print("FizzBuzz")
                break
            if n % 3 == 0:
                print("Fizz")
                break
            if n % 5 == 0:
                print("Buzz")
                break

fizzbuzz()