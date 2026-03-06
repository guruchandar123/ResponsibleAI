import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric
from lime.lime_tabular import LimeTabularExplainer

data = pd.read_csv('dataset.csv')
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

dataset = BinaryLabelDataset(df=pd.concat([X_test, y_test], axis=1), 
                             label_names=['target'], 
                             protected_attribute_names=['gender'])
metric = BinaryLabelDatasetMetric(dataset, unprivileged_groups=[{'gender': 0}], 
                                  privileged_groups=[{'gender': 1}])
print(metric.disparate_impact())

explainer = LimeTabularExplainer(X_train.values, feature_names=X_train.columns)
exp = explainer.explain_instance(X_test.values[0], model.predict_proba)
