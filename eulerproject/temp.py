modulo = 1000000007
#speed up hint: (10e9) % modulo = -7
#init speedup array
shortcut = 18
arr_lookup=[1]*(shortcut+1)
for i in range(1,(shortcut+1)):
    arr_lookup[i]=(10**i)%modulo

def S(i):
    A = i%9
    B = i//9    
    #sum = (1+..+A)*(10^B) + A*(10^B-1) + 45*(10^(B-1)) + 9*(10^(B-1)-1) + 45*(10^(B-2)) + 9*(10^(B-2)-1) + ... + 45*10 + 9*9 +45
    #sum = (A(A+1)/2)*(10^B) + A*(10^B) - A +(9+45)*(10^(B-1) + .. + 1) - 9*B
    #sum = (10^B) * (A(A+1)/2 + A) - A - 9*B + 6*(10-1)*(10^(B-1) + .. + 1) = (10^B) * (A(A+1)/2 + A) - A - 9*B + 6*(10^B -1)
    #sum = (10^B) * (A(A+1)/2 + A + 6) - (A + 9*B + 6)
    #since (7,10e9+7)=1; 7^(10e9+7 - 1)%(10^9+7)=1
    #B = 18C+R
    
    C = B//18
    R = B%18
    C = C%(int((modulo-1)/2))
    D = 1
    print (C)
    for j in range(0,C):
        D = (D*49)%modulo

    D = (D)*(arr_lookup[R])
    D = D% modulo
    
    S = D*(A+6+ int(A*(1+A)/2))- (A + 9*B + 6)
    S = S%modulo
    
    return S

#init f(i) to 90
arr_f=[0]*91
arr_f[1]=1
for i in range(2,91):
    arr_f[i]=arr_f[i-1]+arr_f[i-2]

result = 0
for i in range(2,91):
    result += S(arr_f[i])
    result = result % modulo
    print (i,result)

print (result)
