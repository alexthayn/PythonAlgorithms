# Clearwater Analytics Interview Questions
# Given a cube made up of n x n x n smaller cubes, 
# write a  function that finds the number of smaller cubes with at least one face showing.

def numCubesOnOutside(n):
    #get total num of cubes remove the inner (n-2)*(n-2)*(n-2) cubes
    return (n*n*n) - ((n-2)*(n-2)*(n-2))

# Merge two sorted arrays
def mergeArrays(arr1, arr2):
    mergedArray = [None]*(len(arr1)+ len(arr2))
    i = index1 = index2 = 0    
    while(index1 < len(arr1) and index2 < len(arr2) and i < (len(mergedArray))):
        if(arr1[index1] <= arr2[index2]):
            mergedArray[i] = arr1[index1]
            index1 += 1
        else:
            mergedArray[i] = arr2[index2]
            index2 += 1
        i += 1

    while(index1 < len(arr1) and i < len(mergedArray)):
        mergedArray[i] = arr1[index1]
        index1 += 1
        i += 1

    while(index2 < len(arr2) and i < len(mergedArray)):
        mergedArray[i] = arr2[index2]
        index2 += 1
        i += 1

    return mergedArray

            
if __name__ == "__main__":
    n = 3
    answer = numCubesOnOutside(n)
    print("A %dx%dx%d cube has %s cubes with at least one face showing"%(n,n,n,answer))

    n = 4
    answer = numCubesOnOutside(n)
    print("A %dx%dx%d cube has %s cubes with at least one face showing"%(n,n,n,answer))
    
    n = 5
    answer = numCubesOnOutside(n)
    print("A %dx%dx%d cube has %s cubes with at least one face showing"%(n,n,n,answer))


    print("Merge two sorted arrays:")
    a = [2,6,7,10]
    print(a)
    b = [1,4,6,8,8,10]
    print(b)
    print("After merge: ")
    print(mergeArrays(a,b))
