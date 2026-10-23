# Question 4
# WAP to create a function that print the first 15 elements of fibonacci series without recursion.
def fib(n):
    if n < 1:
        return n
    return fib(n-1) + fib(n-2)

print("First 15 fibonacci numbers:")
for i in range(15):
    print(fib(i), end=" ")