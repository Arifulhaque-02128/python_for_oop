# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q

string = input().split()
length = len(string)

for i in range(length) : 
    st = string[i]
    rev_st = st[::-1]
    if(i == length-1) :
        print(rev_st)
    else : print(rev_st, end=" ")
