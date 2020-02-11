import matplotlib.pyplot as plt
plt.style.use('dark_background')
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
fig, ax = plt.subplots()
ax.scatter(5,15,s=200)
ax.scatter(1,3,s=200)
ax.scatter(8,40,s=200)

#set chart titles  and axes
ax.set_title("Squares")
ax.set_xlabel("Values")
ax.set_ylabel("Squares")

plt.show()