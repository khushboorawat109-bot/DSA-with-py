def find_min_max(arr,start,end):
    if(start==end):
        return arr[start], arr[end]
    if(start+1==end):
        if(arr[start]<arr[end]):
            return arr[start] , arr[end]
        else:
            return arr[end], arr[start]

    mid = (start+end)//2 
    min1 , max1 = find_min_max(arr,start,mid)
    min2 , max2 = find_min_max(arr,mid+1,end)
    
    final_min=min(min1, min2)
    final_max=max(max1, max2)
    return final_min , final_max

arr=[23,14,45,3,6,10]
min_val , max_value =find_min_max(arr,0,len(arr)-1)
print("minimum value is :", min_val)
print("maximum value is :", max_value)           

                    