def is_perfect_square(num):
    return int(num**0.5)**2 == num

def sum_of_digits_less_than_10(num):
    return sum(map(int, str(num))) < 10
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
result_list = [num for num in range(start_range, end_range + 1) if is_perfect_square(num) and sum_of_digits_less_than_10(num)]
print("List of perfect squares with a sum of digits less than 10:", result_list)
