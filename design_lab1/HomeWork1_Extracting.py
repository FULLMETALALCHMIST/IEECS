def extracting(guess, number):
    while guess * guess - number > 0.0001 or number - guess * guess > 0.0001:
        guess = (guess + number / guess) / 2.0
    else:
        print(f'The answer is {guess}')


input_number = float(input('Please input a number'))
input_guess = float(input('Please input your guess'))

extracting(input_guess, input_number)

# Test
# extracting(16, 4)
# The answer is 4.000001387732445
