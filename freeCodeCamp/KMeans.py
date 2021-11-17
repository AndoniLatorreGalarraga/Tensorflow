import matplotlib.pyplot as plt
import random, time

k = 4

#generate data
x = []
y = []

for i in range(k):
    centroid = (random.random(), random.random())
    n = random.randint(10, 30)
    for j in range(n):
        x.append(random.normalvariate(centroid[0], 0.03))
        y.append(random.normalvariate(centroid[1], 0.03))
plt.figure(0)
plt.scatter(x, y, c='red')

#k means
xc = []
yc = []
c = []
for i in range(k):
    xc.append(random.random())
    yc.append(random.random())
    c.append(random.uniform(0,10))

plt.figure(1)
plt.scatter(x, y, c='red')
plt.scatter(xc, yc, c=c)

plt.show()
