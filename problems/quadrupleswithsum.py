from itertools import combinations
a=[2,7,4,0,9,5,1,3]
sum_num=20
comb = combinations(a, 4)
for i in list(comb):
    if(sum(i)==sum_num):
        print (i)

