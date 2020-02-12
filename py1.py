a = 9
x = 1
i = 1

for i in range(a + 1):
    if i > 1 and a / i > 1 and a % i == 0:
        x *= i
        i = i
print(x)
