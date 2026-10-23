# Question 1
# WAP to print the second largest and second smallest element in a list of 10 integers without using sorting function.
def second_min_max(lst):
    first_max = second_max = float('-inf')
    first_min = second_min = float('inf')
    for x in lst:
        if x > first_max:
            second_max, first_max = first_max, x
        elif first_max > x > second_max:
            second_max = x
        if x < first_min:
            second_min, first_min = first_min, x
        elif first_min < x < second_min:
            second_min = x
    return second_min, second_max

nums = list(map(int, input("enter 10 nos").split()))
smin, smax = second_min_max(nums)
print("smallest:", min(nums), "second smallest:", smin)
print("larger:", max(nums), "second larger:", smax)