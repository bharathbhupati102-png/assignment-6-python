# Question 3
# WAP to create an integer list of 20 elements increase the odd values elements by 5.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(number_list)):
    if number_list[i] % 2 != 0:
        number_list[i] += 5
print(number_list)