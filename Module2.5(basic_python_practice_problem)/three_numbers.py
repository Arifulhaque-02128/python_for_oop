# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Z

value = input().split()

k = int(value[0])
s = int(value[1])

count = 0

for i in range(k) :
    for j in range(k) :
        if(s >= (i+j) and s-i-j <= k) :
            count += 1

print(count)