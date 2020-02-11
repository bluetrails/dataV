import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [ x ** 3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(x_values,y_values, c='red')
plt.show()