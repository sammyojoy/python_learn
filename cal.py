def addmultiplenumbers(numbers):
    # Calculate the sum of numbers in the list
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    result = 1
    # Multiply each number in the list
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    # Check if the number is even
    return num % 2 == 0

def isitaninteger(num):
    # Check if the number is an integer
    return isinstance(num, int)


def main():
    print("Hello learners!")

    # Example usage of the functions
    numbers = [2, 3, 5, 7]
    print("Sum of numbers:", addmultiplenumbers(numbers))
    print("Product of numbers:", multiplymultiplenumbers(numbers))
    print("Is 4 even?", isiteven(4))
    print("Is 4 an integer?", isitaninteger(4.0))


if __name__ == "__main__":
    main()