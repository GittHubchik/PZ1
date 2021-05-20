import numpy as np
import matplotlib.pylab as plt
import csv
import os.path

x = np.arange(-512,512,1)
A = 512

def f(x):
    return -(A + 47) * np.sin(np.sqrt(abs(x / 2 +
                (A + 47)))) - x * np.sin(np.sqrt(abs(x - (A + 47))))

plt.grid()
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f (x)')
plt.show()

if not os.path.exists('results'):
    os.mkdir('results')
res_name = os.path.join(os.getcwd(),'results','task_01_40-506C_Sukharev_07.txt')

with open(res_name, 'w') as txtfile:
    txtfile.write('x{0:4}f(x)\n'.format(' '))
    for i in range(len(x)):
        txtfile.write('{0}{1:4}{2}\n'.format(str(x[i]), ' ', str(f(x[i]))))
