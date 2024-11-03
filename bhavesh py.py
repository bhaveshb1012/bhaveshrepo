'''import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 400)
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3
plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='black', linestyle='-', label='y = 2x + 1')
plt.plot(x, y2, color='grey', linestyle='--', label='y = 2x + 2')
plt.plot(x, y3, color='silver', linestyle=':', label='y = 2x + 3')
plt.title("Graphs of y = 2x + 1, y = 2x + 2, and y = 2x + 3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='black', marker='+')
plt.title("Scatter Plot of Points (x, y)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()'''

'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weight-height.csv")

height_inches = data['Height']
weight_pounds = data['Weight']

height_cm = height_inches * 2.54

weight_kg = weight_pounds * 0.453592

mean_height_cm = np.mean(height_cm)
mean_weight_kg = np.mean(weight_kg)

print(f"Mean Height (cm): {mean_height_cm}")
print(f"Mean Weight (kg): {mean_weight_kg}")

plt.figure(figsize=(8, 5))
plt.hist(height_cm, bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Heights (in cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()'''

'''import numpy as np
A = np.array([
    [4, 7],
    [2, 6]
])
A_inv = np.linalg.inv(A)
I1 = np.dot(A, A_inv)
I2 = np.dot(A_inv, A)
print("A * A_inv:\n", I1)
print("A_inv * A:\n", I2)
identity_matrix = np.eye(A.shape[0])
print("\nIs A * A_inv close to identity? ", np.allclose(I1, identity_matrix))
print("Is A_inv * A close to identity? ", np.allclose(I2, identity_matrix))'''

