def reversearray(arr): 
    newarr = []
    for i in range(len(arr) - 1, -1, -1): 
        newarr.append(arr[i])
    return newarr

print(reversearray([1,2,3,4]))
print(reversearray([5,6,7,2,1]))