def max(list):
    maxnum = list[0]

    for nums in list:
        if nums > list[0]:
            maxnum = nums 
    return maxnum

NumbersList = [1, 3, 4, 5, 6, 7]

print("The Maximum Number is: ")
print(max(NumbersList))