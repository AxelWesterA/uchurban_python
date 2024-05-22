import random as rnd


a = rnd.randint(3, 20)
print(a)
list_ = []
list_sum = []
for i in range(1, a):
    list_.append(i)

print(list_)

for i in range(1, a):
    for j in range(2, a):
        if i <= a // 2:
            if a % (i + j) == 0:
                if i == j:
                    continue
                else:
                    list_sum.append(i)
                    list_sum.append(j)

print(list_sum)
