s={1,2,3,4,5.2, 4.9, 3.6,6.0}
print(id(s))
print(s)
s.add(16j)
print(s)
print(id(s))

,,, output
1950097543840
{1, 2, 3, 4, 5.2, 4.9, 3.6, 6.0}
{1, 2, 3, 4, 5.2, 4.9, 3.6, 6.0, 16j}
1950097543840
,,,