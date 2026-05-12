import matplotlib.pyplot as plt

x_values = [0,1,2,3,4,5]
y_values1 = [10,13,15,18,16,20]
y_values2 = [9,11,18,19,17,19]

plt.plot(x_values,y_values1)
plt.plot(x_values,y_values2)
plt.savefig('gen_files/graphs/linegraph.png')
plt.show()
plt.close()


plt.scatter(x_values, y_values1)
plt.scatter(x_values, y_values2)
plt.savefig('gen_files/graphs/scatterplot.png')
plt.show()
