def linear(array,target):
    for i in range(0,5):
        if array[i]==target:
            return i
array=[10,20,30,87,25]
target=int(input("enter target value:"))
result=linear(array,target)
if result != -1:
    print("element found at index:",result)
else:
    print("element not found")                