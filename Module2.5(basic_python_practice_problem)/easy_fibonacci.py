# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y

n = int(input())

if(n == 1) :
    print(0)

else :
    fibo = [0, 1]

    for i in range(2, n) :
        result = fibo[i-1] + fibo[i-2]
        fibo.append(result)


    for val in fibo :
        print(val, end=" ")