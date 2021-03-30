# # def hourglass(arr): 
#     for i in range(0, len(arr)): 
        


def hgsumindex(arr, i, j):
    hourglasssum = 0
    hourglasssum = arr[0+i][0+j] + arr[0+i][1+j] + arr[0+i][2+j] + arr[1+i][1+j] + arr[2+i][0+j] + arr[2+i][1+j] + arr[2+i][2+j]
    return hourglasssum                  
      
arr1 = [
    [1,2,3,4,5,1],
    [2,3,4,5,6,2],
    [3,0,1,2,3,0],
    [8,1,2,3,3,2],
    [1,1,2,5,1,2],
    [3,2,1,1,5,7]
]

arr2 = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

arr3 = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]

# h1 = hgsumindex(arr1, 0, 0)
# h2 = hgsumindex(arr1, 0, 1)
# h3 = hgsumindex(arr1, 0, 2)
# h4 = hgsumindex(arr1, 0, 3)
# h5 = hgsumindex(arr1, 1, 0)
# h6 = hgsumindex(arr1, 1, 1)
# h7 = hgsumindex(arr1, 1, 2)
# h8 = hgsumindex(arr1, 1, 3)
# h9 = hgsumindex(arr1, 2, 0)
# h10 = hgsumindex(arr1, 2, 1)
# h11 = hgsumindex(arr1, 2, 2)
# h12 = hgsumindex(arr1, 2, 3)
# h13 = hgsumindex(arr1, 3, 0)
# h14 = hgsumindex(arr1, 3, 1)
# h15 = hgsumindex(arr1, 3, 2)
# h16 = hgsumindex(arr1, 3, 3)

hgallsum = []
for i in range(0, 4): 
    for j in range(0, 4): 
        hgallsum.append(hgsumindex(arr3, i, j))

maxhg = hgallsum[0]
for n in hgallsum: 
    if(n > maxhg): 
        maxhg = n

print(hgallsum)
print(maxhg)
        

