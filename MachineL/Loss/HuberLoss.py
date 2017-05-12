import numpy as np
import matplotlib.pyplot as plt


# Huber loss是为了增强平方误差损失函数（squared loss function）对噪声（或叫离群点，outliers）的鲁棒性提出的。
def huber_loss(e, d):
    return (abs(e) <= d) * e ** 2 / 2 + (e > d) * d * (abs(e) - d / 2)


plt.figure(figsize=(6, 4.5), facecolor='w', edgecolor='k')
x = np.arange(-20, 20)
plt.plot(x, x ** 2 / 2, label='squared loss', lw=2)
for d in (10, 5, 3, 1):
    # here we can see how to show delta in image.
    plt.plot(x, huber_loss(x, d), label=r'huber loss: $\delta$={}'.format(d), lw=2)

plt.legend(loc='best', frameon=False)
plt.xlabel('standard deviation')
plt.ylabel('loss')
plt.show()
