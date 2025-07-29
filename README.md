TASK 1 :

🌸 Iris Flower Classification:

Classifying iris flower species using various machine learning models.

📁 Dataset:

Used: IRIS.csv

Features:

sepal length

sepal width

petal length

petal width

species (target)

🔧 Step 1: Load and Understand Data:

Loaded dataset using pandas

Explored data with .info() and .describe()

🧹 Step 2: Encode Labels:

Used LabelEncoder to convert species names to numeric values

Classes encoded as integers: e.g., setosa → 0, versicolor → 1, virginica → 2

🧪 Step 3: Prepare Data:

Separated features (X) and target (y)

Split data into training and testing sets (80% train, 20% test)

🤖 Step 4: Logistic Regression Model:

Trained a LogisticRegression model

Evaluated:

Training accuracy

Testing accuracy

📊 Step 5: Model Evaluation:

Used confusion_matrix and classification_report to evaluate performance

Compared predicted vs actual values on the test set

⚙️ Step 6: Compare Multiple Models:

Tested these models:

Logistic Regression

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Decision Tree

Random Forest

Printed accuracy for each model on the test data.

📈 Step 6.2: Visualize Model Accuracies:

Plotted a horizontal bar chart to compare model accuracies

Set x-axis limit: 0.90 to 1.00 for clear visualization

🛠️ Tools Used:

Python

pandas

matplotlib

scikit-learn
