import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
y_values1 = [10, 13, 15, 18, 16, 20]
y_values2 = [9, 11, 18, 19, 17, 19]

plt.plot(x_values, y_values1, marker='o', color='b', label='Line 1')
plt.plot(x_values, y_values2, marker='s', color='r', label='Line 2')

plt.legend()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Graph Title')
plt.grid(True)
plt.show()
