import math

'''
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def main():
    arr1=[1,2,3,4,5]
    arr2=[3,2,1]

    '''
    arr1t = []
        arr1t.append(math.prod(arr1[1::]))
        print(arr1t)
        #i+1::
    
        print(arr1[1+1::])
        print(arr1[1-1::-1])
        print(arr1)
        # i + 1
        for i in range(1,len(arr1)):
            print(math.prod(arr1[i+1::])*math.prod(arr1[i-1::-1]))
    '''
    print(findProductOfArrayExceptFori(arr1))
    print(findProductOfArrayExceptFori(arr2))

def findProductOfArrayExceptFori(arr):
    arr1t = []
    arr1t.append(math.prod(arr[1::]))
    for i in range(1,len(arr)):
        arr1t.append(math.prod(arr[i+1::])*math.prod(arr[i-1::-1]))
    return arr1t
main()