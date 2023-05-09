# a = (23,44,24,33,66,45)
# 2. write a program to add 60 to the above mentioned tuple.


a = (23,44,24,33,66,45)
b = list(a)
print(b)
b.append(60)
print(b)
a = tuple(b)
print(a)
