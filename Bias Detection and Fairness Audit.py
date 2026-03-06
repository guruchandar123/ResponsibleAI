import pandas as pd

def audit_fairness(data, protected_attribute, target_column):
    # Calculate selection rates for different groups
    groups = data.groupby(protected_attribute)[target_column].mean()
    
    privileged_rate = groups.max()
    unprivileged_rate = groups.min()
    
    disparate_impact = unprivileged_rate / privileged_rate
    
    status = "PASS" if 0.8 <= disparate_impact <= 1.25 else "FAIL"
    
    return {
        "disparate_impact_ratio": round(disparate_impact, 4),
        "audit_status": status,
        "recommendation": "Maintain monitoring" if status == "PASS" else "Requires mitigation"
    }

# Sample Data: 'Gender' (0=Male, 1=Female), 'Approved' (1=Yes, 0=No)
df = pd.DataFrame({
    'gender': [0, 0, 0, 0, 1, 1, 1, 1],
    'approved': [1, 1, 1, 0, 1, 0, 0, 0]
})

results = audit_fairness(df, 'gender', 'approved')
print(f"Fairness Audit Results: {results}")
