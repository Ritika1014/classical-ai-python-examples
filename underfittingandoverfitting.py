import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# 1. Create a nonlinear dataset
np.random.seed(0)
X = np.linspace(0, 10, 50)
y = np.sin(X) + np.random.normal(0, 0.2, 50)

X = X.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. UNDERFITTING MODEL (Linear Regression)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X)
# 3. GOOD FIT (Polynomial degree = 3)
poly3 = PolynomialFeatures(degree=3)
X_poly3 = poly3.fit_transform(X)

model_poly3 = LinearRegression()
model_poly3.fit(poly3.fit_transform(X_train), y_train)
y_pred_poly3 = model_poly3.predict(X_poly3)

# 4. OVERFITTING (Polynomial degree = 10)
poly10 = PolynomialFeatures(degree=10)
X_poly10 = poly10.fit_transform(X)

model_poly10 = LinearRegression()
model_poly10.fit(poly10.fit_transform(X_train), y_train)
y_pred_poly10 = model_poly10.predict(X_poly10)

# 5. Plot all curves
plt.figure(figsize=(12, 6))
plt.scatter(X, y, label='Actual Data')

plt.plot(X, y_pred_linear, label='Underfitting (Linear)', linewidth=2)
plt.plot(X, y_pred_poly3, label='Good Fit (Degree 3)', linewidth=2)
plt.plot(X, y_pred_poly10, label='Overfitting (Degree 10)', linewidth=2)

plt.title("Underfitting vs Good Fit vs Overfitting")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
