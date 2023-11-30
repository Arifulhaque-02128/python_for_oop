# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q
n = int(input())
nums = []
for i in range(n) : 
    num = input()
    nums.append(num)

# print("output : ")
for num in nums :
    num = num[: : -1]
    for val in num :
        print(val, end=" ")
    print(end="\n")
    