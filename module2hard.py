import random

result = []
n = int(random.randrange(3,20))
print('Случайное число: ', n)

for i in range(1,(n//2)+1):
     for j in range(2,(n-i+1)):
        if n % (i+j) == 0 and i!=j:
            result.append(i)
            result.append(j)
print("Пароль: ",*result)