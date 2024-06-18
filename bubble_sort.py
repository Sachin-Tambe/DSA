my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1): # 5 - 1 = 4
    swapped = False
    for j in range(n-i-1): # 5 - 0 - 1 = 4
        if my_array[j] > my_array[j+1]: # 7 > 3 
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j] # my_array[j], my_array[j+1] = 3 , 7
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)