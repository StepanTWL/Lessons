import random

import seaborn as sns
from matplotlib.pyplot import *

"""
a = list(range(0, 20))
b = list(range(20, 0, -1))
title('Test')
plot(a, '-o', color='red')
plot(b, '-o', color='red')


names = ['apple', 'banana', 'orange']
counts = [34, 80, 55]

bar(names, counts)
title('Fruits')
xlabel('Fruits')
ylabel('Count')
grid(True)


ion()#разрешение анимации

while True:
    rand_value = random.randint(10_000_000, 99_999_999)
    np.random.seed(rand_value)
    data = np.random.randn(25, 25)
    imshow(data, cmap='spring')
    show()
    pause(0.3)



cat_par = [i for i in range(1, 6)]
g1 = [10, 21, 34, 12, 27]
g2 = [17, 15, 25, 21, 26]
width = 0.3
x = np.arange(len(cat_par))

fig, ax = subplots()
rects1 = ax.bar(x - width/2, g1, width, label='g1')
rects2 = ax.bar(x - width/2, g2, width, label='g2')
ax.set_xticks(x)
ax.set_xtickslabels(cat_par)
legend()
show()



flights = sns.load_dataset('flights')
sns.set_style('darkgrid')
sns.lineplot(x='year', y='passengers', data=flights)
show()
"""


sns.set_style('darkgrid')
x = [random.randint(10, 100) for i in range(10)]
y = [random.randint(10, 100) for i in range(10)]
sns.lineplot(x)
show()