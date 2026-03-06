import numpy as np

def add_laplace_noise(data, sensitivity, epsilon):
    noise = np.random.laplace(0, sensitivity/epsilon, len(data))
    return data + noise

sensitive_counts = np.array([10, 50, 100])
dp_data = add_laplace_noise(sensitive_counts, 1, 0.5)
print(dp_data)
