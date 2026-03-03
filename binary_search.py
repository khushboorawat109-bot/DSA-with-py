def binary(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
array=[10,20,30,45,55] 
target=45
result=binary(array,target)
if result != -1:
    print("element found at index:",result)
else:
    print("element not found")                       