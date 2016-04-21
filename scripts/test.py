from random import *


x = [[i] for i in range(10)]
print(x)

shuffle(x)
print(x)

print 'random.sample'
for i in range(5):
    print sample(x, 1)[0]

print 'random.choice'
for i in range(5):
    print choice(x)