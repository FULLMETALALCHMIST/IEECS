def cube(original_number):

    first_iteration = original_number
    last_iteration = first_iteration - ((first_iteration**3 - original_number)/(3*first_iteration**2))

    while abs(last_iteration - first_iteration) > 0.01:
        first_iteration = last_iteration
        last_iteration = first_iteration - ((first_iteration**3 - original_number) / (3 * first_iteration ** 2))

    print(f'The cube of the original number {original_number} is {last_iteration}')


your_number = float(input('Please input your number'))

cube(your_number)

# Test
# cube(8)——2.00004628653597
# cube(0.125)——0.5000021811888423
# cube(-8)——2.00004628653597
