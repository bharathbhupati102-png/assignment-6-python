# Question 2
# WAP to create two list containing 5 integers and second list containing 5 strings,
#  print both the list one element from each list combined at a time.
nums = [1, 2, 3, 4, 5]
str = ['apple', 'banana', 'cherry', 'elderberry']
for n, s in zip(nums, str):
    print(n, s)