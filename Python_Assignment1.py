lst= []
for n in range(2000,3200):
    if n%7 ==0 and n%5 != 0:
        lst.append(n)
print(*lst, sep=",")
