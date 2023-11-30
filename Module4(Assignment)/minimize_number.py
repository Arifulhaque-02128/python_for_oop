# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
n = int(input())
input1 = input().split()
num_list = [int(val) for val in input1]

cnt = 0
flag = True
while flag : 
    for idx, num in enumerate(num_list) :
        if(num%2 != 0) : 
            flag = False
            break
        else : 
            num_list[idx] = num/2
    cnt += 1

print(cnt-1)