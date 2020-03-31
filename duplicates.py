import sys,os


s = "abacdleachd"

l = list(s)

index = 0
for i in range(0,len(l)) :
	for j in range(0, i + 1)  :
		if l[i] == l[j] :
			break;

	if i == j :
		l[index] = l[i]
		index += 1

print (l[:index])
