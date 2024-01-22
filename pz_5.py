def func(start_of_range: int, end_of_range: int):
    summary_of_range = 0
    for i in range(start_of_range, end_of_range + 1):
        summary_of_range += i
    return summary_of_range

print(func(1, 5))