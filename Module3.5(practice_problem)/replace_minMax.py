# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
import math

n = int(input())
values = input().split()
nums = []
minVal = math.inf
maxVal = -math.inf
minIdx = -1
maxIdx = -1
for idx, v in enumerate(values) :
    val = int(v)
    nums.append(val)
    if(val <= minVal) :
        minVal = val
        minIdx = idx
    if(val >= maxVal) :
        maxVal = val
        maxIdx = idx

nums[minIdx] = maxVal
nums[maxIdx] = minVal

for num in nums :
    print(num, end=" ")

