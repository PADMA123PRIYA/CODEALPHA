#step 1
import pandas as pd
iris_df = pd.read_csv("IRIS.csv")

print(iris_df.info())
print(iris_df.describe())

#step 2
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
iris_df['species'] = le.fit_transform(iris_df['species'])

print(iris_df['species'].unique())

#step 3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
iris_df['species'] = le.fit_transform(iris_df['species'])
X = iris_df.drop('species', axis=1)
y = iris_df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#step 4
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
train_acc = lr_model.score(X_train, y_train)
test_acc = lr_model.score(X_test, y_test)

print("Training Accuracy:", train_acc)
print("Test Accuracy:", test_acc)

#step5
from sklearn.metrics import classification_report, confusion_matrix
y_pred = lr_model.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Classification report
cr = classification_report(y_test, y_pred)
print("Classification Report:\n", cr)


#step 6
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#step 6.1
models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}
for name, model in models.items():
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"{name} Accuracy: {acc:.2f}")

#5step 6.2
import matplotlib.pyplot as plt
model_names = []
accuracies = []

for name, model in models.items():
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    model_names.append(name)
    accuracies.append(acc)

# Plot
plt.figure(figsize=(8, 5))
plt.barh(model_names, accuracies, color='skyblue')
plt.xlabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.xlim(0.9, 1.01)
plt.grid(axis='x', linestyle='--')
plt.show()


