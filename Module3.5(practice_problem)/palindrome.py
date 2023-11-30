# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G
n = int(input())
values = input().split()
nums = []
for val in values :
    nums.append(int(val))

nums_rev = nums[::-1]

if(nums == nums_rev) : print("YES")
else : print("NO")