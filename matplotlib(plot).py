import matplotlib.pyplot as plt
# ---------------- LINE PLOT ----------------
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Line Plot")

# ---------------- BAR CHART ----------------
categories = ['A', 'B', 'C', 'D']
values = [30, 45, 20, 60]

plt.subplot(2, 3, 2)
plt.bar(categories, values)
plt.title("Bar Chart")

# ---------------- SCATTER PLOT ----------------
x2 = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 7, 8]

plt.subplot(2, 3, 3)
plt.scatter(x2, y2)
plt.title("Scatter Plot")

# ---------------- HISTOGRAM ----------------
data = [10,20,20,30,30,30,40,50,50,60]

plt.subplot(2, 3, 4)
plt.hist(data, bins=5)
plt.title("Histogram")

# ---------------- PIE CHART ----------------
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]

plt.subplot(2, 3, 5)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()
