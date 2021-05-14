import math
import numpy as np


n = 100
T = 1.

times = np.linspace(0.,T,n)
# print(times)


# print(np.random.normal(0,0.1))


# print(np.random.randn(2, 1))


print((np.diag([1.0, np.deg2rad(30.0)]) ** 2) @ np.random.randn(2, 1))