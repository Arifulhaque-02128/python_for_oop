# https://atcoder.jp/contests/arc087/tasks/arc087_a

n = int(input())
input1 = input().split()

num_list = [int(num) for num in input1]
num_set = set(num_list)

res = 0
for num in num_set :
    cnt = num_list.count(num)
    
    if( cnt > num) :
        diff = cnt - num
        res += diff
    elif(cnt < num) : 
        res += cnt

print(res)