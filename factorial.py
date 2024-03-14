def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    user_input=int(input("enter the number"))
    result=factorial(user_input)
    print("the factorial of{user_input}is:",{result})
