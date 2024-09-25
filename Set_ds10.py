s={11,12,13,17,16,21,28}
print(s)
print("length of set is:" ,len(s))
s.discard(77)
print(s)
print("length of set is:",len(s))
s.discard(21)
print(s)
print("length of set is:",len(s))

'''
E:\DS>python Set_ds10.py
{16, 17, 28, 21, 11, 12, 13}
length of set is: 7
{16, 17, 28, 21, 11, 12, 13}
length of set is: 7
{16, 17, 28, 11, 12, 13}
length of set is: 6
'''