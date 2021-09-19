
number = float(input('Please input a number'))

guess = float(input('Please input a guess number'))

while guess * guess - number > 0.0001 or number - guess * guess > 0.0001:

    guess = (guess + number / guess) / 2


print(guess)
