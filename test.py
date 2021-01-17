import math
import random
print('Program to generate addition problems')
for i in range(0, 100):
    sum = ' '+str(random.randint(10, 99))+'\nx' + \
        str(random.randint(10, 99))+'\n----\n----\n'
    f1 = open('mutliplication_sums1.txt', 'a')
    f1.write(sum)
    f1.close
