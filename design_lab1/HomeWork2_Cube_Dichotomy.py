def main(cube):

    positive_num = abs(cube)

    if positive_num > 1:

        high = positive_num
        low = 0.0
        guess_number = (high + low) / 2.0
    else:

        low = positive_num
        high = 1.0
        guess_number = (high + low) / 2.0

    while abs(guess_number ** 3 - positive_num) > 0.0000001:
        if guess_number ** 3 < positive_num:
            low = guess_number
        else:
            high = guess_number
        guess_number = (high + low) / 2.0

    if cube >= 0:
        print(f'The cube of the original number {cube} is {guess_number}')
    else:
        print(f'The cube of the original number {cube} is {-guess_number}')


your_number = float(input('Please input your number'))
main(your_number)

# Test
# main(8)——2.0
# main(-8)——2.0
# main(0.125)——0.5000000298023224
# main(-0.125)——-0.5000000298023224

