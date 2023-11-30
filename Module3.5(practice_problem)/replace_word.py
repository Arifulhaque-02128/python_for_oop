# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/V

values = input().split("EGYPT")
length = len(values)
for idx, val in enumerate(values):
    if(idx == length - 1 ) : print(val)
    else : print(val, end=" ")