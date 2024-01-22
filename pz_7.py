def func(number):
    number_str = str(number)
    first_half = number_str[0:3]
    second_half = number_str[3:6]

    sum_first_half = 0
    sum_second_half = 0

    for i in first_half:
        sum_first_half += int(i)

    for j in second_half:
        sum_second_half += int(j)

    if sum_first_half == sum_second_half:
        print("Это счастливое число")
    else:
        print("Это несчастливое число")


func(123123)