numbers = [-4,1,8, -9, 6]
 
# Sorting list of Integers
numbers.sort()
size=len(numbers)
if((numbers[0]*numbers[1]*numbers[size-1])<(numbers[size-3]*numbers[size-2]*numbers[size-1])):
    max_prod=numbers[size-3]*numbers[size-2]*numbers[size-1]
else:
    max_prod=(numbers[0]*numbers[1]*numbers[size-1])
        

    
print(max_prod)
