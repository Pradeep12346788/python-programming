def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in numbers_str.split()]
prime_count = 0
composite_count = 0
for number in numbers:
    if is_prime(number):
        prime_count += 1
    else:
        composite_count += 1
print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", composite_count)
