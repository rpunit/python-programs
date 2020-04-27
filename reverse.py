

s = "12345678"
l = list(s)

tl = len(l)
mid = len(l)//2
for i in range(mid):
	l[i],l[tl - i - 1] = l[tl-i - 1], l[i]


print ("".join(l))
