<<<<<<< HEAD
def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
a=[64,34,25,45,40,51,2] 
insertionSort(a) 
=======
def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
a=[64,34,25,45,40,51,2] 
insertionSort(a) 
>>>>>>> 8afebed376519e1884e22e7122f660b0a548d3f4
print ("Sorted array is:",a)      