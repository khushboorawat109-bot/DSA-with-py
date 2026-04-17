<<<<<<< HEAD
def Max_min_diff(arr):
    arr.sort()
    n=len(arr)
    mid=n//2
    max=0
    min=0
    j=n-1
    for i in range(mid):
        max=max+abs(arr[i]-arr[j])
        j=j-1
        min=min+ abs(arr[2*i]-arr[2*i+1])
    print("Max Difference:",max)
    print("Min Difference:",min)

arr=[12,5,25,10,2,15,8,30]
=======
def Max_min_diff(arr):
    arr.sort()
    n=len(arr)
    mid=n//2
    max=0
    min=0
    j=n-1
    for i in range(mid):
        max=max+abs(arr[i]-arr[j])
        j=j-1
        min=min+ abs(arr[2*i]-arr[2*i+1])
    print("Max Difference:",max)
    print("Min Difference:",min)

arr=[12,5,25,10,2,15,8,30]
>>>>>>> 8afebed376519e1884e22e7122f660b0a548d3f4
Max_min_diff(arr)        