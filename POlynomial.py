# def → “I am creating a function”
# calculate → function name (what it does)
# (x, a, b) → inputs (values we give)
# x: int → x should be an integer (number)
# -> int → function will return an integer

def calculate(x: int, a: int, b: int) -> int: #Make a machine that takes 3 numbers and gives 1 number back
#    return → send answer back
# x**2 → x × x (square)
# a * x**2 → multiply a with x²
# b * x → multiply b with x
# + 1 → add 1
    return a * x**2 + b * x + 1 # we can think in this way also (do the math and give the answer )


def main():#“This is the boss function — it runs everything”
        x = int(input("Enter value of x: "))#input() → ask user to type something
# Enter value of x → message to user
# int() → convert input into number
# x = → store value in x
# Ask user for a number  as x

        a = int(input("Enter value of a: "))
        # Take 3 numbers from user: x, a, b”
        b = int(input("Enter value of b: "))

        result = calculate(x, a, b)
        #Call the function
# Give values (x, a, b)
# Function calculates
# Store answer in result
# Send numbers to machine → get answer back
        print(f"Result: {result}")
#print() → show output
# f"" → formatted string
# {result} → insert value

# Show the answer 



if __name__ == "__main__":#Run this code only if file is started directly
# Start program only when I run this file
    main()#call the main funtion or the boss function 