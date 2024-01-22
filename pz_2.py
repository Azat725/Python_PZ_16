def odd_numbers_between_even_numbers(number_1, number_2):
    for i in range(number_1, number_2):
        if i % 2 != 0:
            print(i, end=" ")
            
            
odd_numbers_between_even_numbers(number_1=1, number_2=10 + 1)