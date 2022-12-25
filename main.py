import matplotlib.pyplot as plt

names = ['Robert', 'Alice', 'Bob', 'Eve', 'John']
salaries = [110000, 95000, 80000, 105000, 75000]

# Create the bar chart
plt.bar(names, salaries, align='center', label='Salary')

# Add labels and title
plt.xlabel('Name')
plt.ylabel('Value')
plt.title('Salary and Age by Name')
plt.legend()

# Show the plot
plt.show()
