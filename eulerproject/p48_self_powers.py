
s = 0
for i in range(1,1001) :
	s += i**i  % 10 ** 10

s = s % 10**10
print (s)

