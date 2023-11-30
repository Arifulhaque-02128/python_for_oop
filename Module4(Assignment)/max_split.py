# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s

s = input() 

l = 0
r = 0
res = []
ans = ''
for val in s :

    if(val == 'L') :
        l += 1
        ans += 'L'
    else : 
        r += 1
        ans += 'R'
    
    if(l == r) :
        res.append(ans)
        ans = ''

length = len(res)
print(length)
for seq in res :
    print(seq)