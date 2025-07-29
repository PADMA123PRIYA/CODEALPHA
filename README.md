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




TASK 2 :

umemployment data analysis

This project uses Python to analyze unemployment data in India from January to November 2020, with a focus on the impact of Covid-19.

📁 About the Data

Source File: Unemployment_Rate_upto_11_2020.csv

Details in the file:

Name of the state (Region)

Date of data (Date)

Unemployment rate (%)

Number of employed people

Labour participation rate

✅ What I Did

Step 1: Data Cleaning
Fixed column names

Changed Date column into proper date format

Step 2: State-wise Trend
Plotted line graphs for each state

Showed how unemployment changed month by month

Step 3: Covid-19 Impact
Compared before March 2020 and after March 2020

Found big rise in unemployment during April–May due to lockdown

Step 4: Month-wise Pattern
Found which months had highest and lowest unemployment

Displayed as a bar chart

Step 5: Final Insights

📈 Highest unemployment: around 43% in April 2020

📉 Lowest unemployment: around 0.4% in August 2020

Covid-19 had a huge effect on job loss

Recovery started slowly after June

📌 Tools Used

Python

pandas

matplotlib

calendar



