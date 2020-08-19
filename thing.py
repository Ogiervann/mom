import random

a = -1
b = 3
n = 1
L = 2

f = open('L' + str(L) + '_' + str(n) + '.txt', 'w')
for i in range(50):
    f.write(str(round(random.expovariate(L), 2)) + '\n')

c = 0
cs = 0
data = []
f.close()
g = open('L' + str(L) + '_' + str(n) + '.txt', 'r')
for line in g:
    data.append([float(x) for x in line.split()])

for i in data:
    c += i[0]
    cs += i[0]*i[0]
f = open('L' + str(L) + '_' + str(n) + '.txt', 'a')
f.write('\nСреднее арифметическое: ' + str(round(c/50, 3)) + '\n' + 'Среднее арифметическое квадратов: ' + str(round(cs/50, 3)))
print(round(c/50, 3), round(cs/50, 3))
g.close()
f.close()
