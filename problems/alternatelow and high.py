def swap( a , first, last ):
    temp = a[first]
    a[first] = a[last]
    a[last] = temp

a = [9,6,8,3,7]
for i in range(1,len(a),2):
    if(a[i-1] > a[i]):
        swap(a,i-1,i)
    if(a[i+1] > a[i] and (i+1) < len(a) ):
        swap(a, i+1,i)
print(a)    
