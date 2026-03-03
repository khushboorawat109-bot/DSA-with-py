import array
val = array.array('i',[1,2,3,4,5])

val.insert(1,20)
val.append(50)
val[0]=22
for i in val:
    print(i) 
