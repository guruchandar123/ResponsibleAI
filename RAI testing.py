import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Setup dummy model
X_train = np.random.rand(100, 5)
y_train = np.random.randint(0, 2, 100)
model = RandomForestClassifier().fit(X_train, y_train)

def robustness_stress_test(model, X_input, noise_level=0.1):
    # Original prediction
    original_pred = model.predict(X_input)
    
    # Add Gaussian noise
    noise = np.random.normal(0, noise_level, X_input.shape)
    X_noisy = X_input + noise
    
    # Noisy prediction
    noisy_pred = model.predict(X_noisy)
    
    # Calculate stability (percentage of unchanged predictions)
    stability = np.mean(original_pred == noisy_pred)
    return stability

# Run test on 10 samples
X_test = np.random.rand(10, 5)
stability_score = robustness_stress_test(model, X_test)
print(f"Model Stability Score: {stability_score * 100}%")
