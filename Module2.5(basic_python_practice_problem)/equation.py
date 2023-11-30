# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F

value = input().split()
x = int(value[0])
n = int(value[1])

if(n < 2) :
    print(0)

else : 
    sum = 0
    for i in range(2, n+1, 2) :
        sum += x**i
    print(sum)

