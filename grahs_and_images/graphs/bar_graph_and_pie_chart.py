import matplotlib.pyplot as plt

# creating a bar graph
categories = ['Cats', 'Dogs', 'Mice', 'Birds']
values = [100, 200, 300, 400]

plt.bar(categories, values)
plt.savefig('gen_files/graphs/bargraph.png')
plt.show()
plt.close()

# creating a pie chart
slices = [100, 200, 300, 400]
labels = ['Cats', 'Dogs', 'Mice', 'Birds']
plt.pie(x=slices, labels=labels, autopct='%.1f%%')
plt.savefig('gen_files/graphs/piechart.png')
plt.show()
plt.close()
