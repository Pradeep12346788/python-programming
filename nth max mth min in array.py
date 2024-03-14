def find_mth_max_and_nth_min(arr, m, n):
    sorted_arr = sorted(arr, reverse=True)
    mth_max = sorted_arr[m - 1] if m <= len(sorted_arr) else None

    sorted_arr = sorted(arr)  # Sort in ascending order
    nth_min = sorted_arr[n - 1] if n <= len(sorted_arr) else None

    return mth_max, nth_min

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

m = int(input("Enter the value of M: "))
n = int(input("Enter the value of N: "))

mth_max, nth_min = find_mth_max_and_nth_min(arr, m, n)

if mth_max is not None and nth_min is not None:
    summation = mth_max + nth_min
    difference = mth_max - nth_min
    print(f"Mth maximum: {mth_max}, Nth minimum: {nth_min}")
    print(f"Sum: {summation}, Difference: {difference}")
else:
    print("Invalid values of M or N. Please check the length of the array.")
