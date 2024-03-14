def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    return sum(range(1, n+1))**2

def main():
    try:
        n = int(input("Enter a natural number: "))
        if n <= 0:
            print("Please enter a positive natural number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid natural number.")
        return

    difference = sum_of_squares(n) - square_of_sum(n)
    print(f"The difference between the sum of the squares and the square of the sum for the first {n} natural numbers is: {difference}")

if __name__ == "__main__":
    main()
