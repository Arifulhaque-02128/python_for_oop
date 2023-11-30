# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S


n = int(input())

for i in range(n) :
    value = input().split()
    x = int(value[0])
    y = int(value[1])
    
    if(x > y) : 
        sum = 0
        for val in range(y+1, x) : 
            if(val%2 == 1) : 
                sum += val

        print(sum)
    
    else : 
        sum = 0
        for val in range(x+1, y) : 
            if(val%2 == 1) : 
                sum += val

        print(sum)