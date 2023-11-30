# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y
input1 = input().split()
n = int(input1[0])
q = int(input1[1])

values = input().split()
nums = list(map(lambda num : int(num), values))
pre_sum = []
for idx, val in enumerate(nums) :
    if(idx == 0) : pre_sum.append(val)
    else : pre_sum.append(pre_sum[idx-1] + val)

for i in range(q) :
    input2 = input().split()
    l = int(input2[0])
    r = int(input2[1])

    sum = 0
    if(l == 1) :
        sum = pre_sum[r-1]
    else :
        sum = pre_sum[r-1] - pre_sum[l-2]

    print(sum)