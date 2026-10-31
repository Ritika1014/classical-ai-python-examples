import numpy as np
from scipy import integrate, optimize, fftpack, stats

# -------------------------------
# 1. Numerical Integration
# Integral of f(x) = x^2 from 0 to 5
# -------------------------------
f = lambda x: x**2
result_integration, _ = integrate.quad(f, 0, 5)
print("Integral of x^2 from 0 to 5 =", result_integration)

# -------------------------------
# 2. Differentiation
# Derivative of sin(x) at x = π/4
# -------------------------------
f = lambda x: np.sin(x)
derivative = optimize.approx_fprime([np.pi/4], f, 1e-6)
print("Derivative of sin(x) at π/4 =", derivative[0])

# -------------------------------
# 3. Solving Equations
# Solve x^2 - 4 = 0
# -------------------------------
eq = lambda x: x**2 - 4
root = optimize.fsolve(eq, 2)   # initial guess = 2
print("Root of equation x^2 - 4 = 0 =", root[0])

# -------------------------------
# 4. Fourier Transform
# -------------------------------
signal = np.array([1, 2, 3, 4])
fft_output = fftpack.fft(signal)
print("FFT of signal [1,2,3,4] =", fft_output)

# -------------------------------
# 5. Basic Statistics (Mean, Median, Std)
# -------------------------------
data = [12, 15, 18, 20, 22]
print("Mean =", stats.tmean(data))
print("Median =", np.median(data))
print("Standard Deviation =", np.std(data))

# -------------------------------
# 6. Optimization (Find minimum of function)
# f(x) = (x-3)^2
# -------------------------------
g = lambda x: (x - 3)**2
min_value = optimize.minimize(g, 0)   # start from x=0
print("Minimum value at x =", min_value.x[0])
