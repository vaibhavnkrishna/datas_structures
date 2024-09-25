a="a2b4c3"
for x in range(len(a)):
	if a[x].isdigit():
		print(a[x])
'''output

2
4
3
'''
a="a2b4c5"
s=""
for x in range (len(a)):
	s1=""
	if a[x].isdigit():
		print(a[x])
		s1=a[x-1]*int(a[x])
	s=s+s1
print(s)
'''
output
2
4
3
2
4
5
aabbbbccccc
'''