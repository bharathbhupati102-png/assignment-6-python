# Question 5
# WAP to create a function that takes list as arguments and returns the even values of the list print the new list.
def get_even_values(lst):
    return [x for x in lst if x % 2 == 0]

arr = [3, 8, 15, 20, 7, 12, 5, 4]
new_list = get_even_values(arr)
print("original list:", arr)
print("new list (even values only):", new_list)