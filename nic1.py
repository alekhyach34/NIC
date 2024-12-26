# -*- coding: utf-8 -*-
"""NIC1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FHLxAeXtFziXBhLE5T_X2y3Ini9nytJp
"""

#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import BaggingClassifier

#Importing dataset
df = pd.read_csv('/content/drive/MyDrive/loan_approval_dataset.csv')

df.columns

df.shape

#Data Information
df.head(10)

df[' loan_status'].value_counts()

print("Shape of the datacolumn: ",df.shape)
df.isna().sum()

df.info()

df.describe()

df.dtypes

df.notnull().sum()

"""**EDA-Exploratory data analysis**"""

sns.countplot(x=' education', data=df)

sns.countplot(x=' self_employed', data=df)

sns.countplot(x=' loan_status', data=df)

# Assuming df is your DataFrame

# Step 1: Encode Categorical Variables
# Example: Using pandas' get_dummies() function for one-hot encoding
df_encoded = pd.get_dummies(df)

# Step 2: Compute Correlation Matrix and Plot Heatmap
# Exclude non-numeric columns before computing correlations
numeric_df = df_encoded.select_dtypes(include=['float64', 'int64'])  # Select numeric columns
corr_matrix = numeric_df.corr()  # Compute correlation matrix
sns.heatmap(corr_matrix, annot=True)  # Plot heatmap

# Show the plot
plt.show()

"""**MODELS**




"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("/content/drive/MyDrive/loan_approval_dataset.csv")

# Drop rows with missing values
df = df.dropna()

# Split features and target variable
X = df.drop(' loan_status', axis=1)
y = df[' loan_status']

# Define columns to be one-hot encoded
categorical_cols = [col for col in X.columns if X[col].dtype == 'object']
numeric_cols = [col for col in X.columns if col not in categorical_cols]

# Define preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Define the model pipeline
rf = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', RandomForestClassifier())])

# Fit the model
rf.fit(X_train, y_train)

# Evaluate the model
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
correlation_matrix = np.corrcoef(y_test, y_pred)
print("Correlation matrix:\n",correlation_matrix)
cm=confusion_matrix(y_test,y_pred)
z1=ConfusionMatrixDisplay(cm).plot()
print("Confusion matrix:\n",cm)

#Logistic Regression
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Define the model pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', LogisticRegression())])

# Fit the model
pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
correlation_matrix = np.corrcoef(y_test, y_pred)
print("Correlation matrix:\n",correlation_matrix)
cm=confusion_matrix(y_test,y_pred)
z2=ConfusionMatrixDisplay(cm).plot()
print("Confusion matrix:\n",cm)

#SVM
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Define the model pipeline
svm = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', SVC())])

# Fit the model
svm.fit(X_train, y_train)

# Evaluate the model
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
correlation_matrix = np.corrcoef(y_test, y_pred)
print("Correlation matrix:\n",correlation_matrix)
cm=confusion_matrix(y_test,y_pred)
z3=ConfusionMatrixDisplay(cm).plot()
print("Confusion matrix:\n",cm)

#KNN
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Define the model pipeline
knn = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', KNeighborsClassifier())])

# Fit the model
knn.fit(X_train, y_train)

# Evaluate the model
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
correlation_matrix = np.corrcoef(y_test, y_pred)
print("Correlation matrix:\n",correlation_matrix)
cm=confusion_matrix(y_test,y_pred)
z4=ConfusionMatrixDisplay(cm).plot()
print("Confusion matrix:\n",cm)

#Decision Tree
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Define the model pipeline
dt = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', DecisionTreeClassifier())])

# Fit the model
dt.fit(X_train, y_train)

# Evaluate the model
y_pred = dt.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
correlation_matrix = np.corrcoef(y_test, y_pred)
print("Correlation matrix:\n",correlation_matrix)
cm=confusion_matrix(y_test,y_pred)
z5=ConfusionMatrixDisplay(cm).plot()
print("Confusion matrix:\n",cm)

#Tabu Search
import numpy as np
import pandas as pd

# Load dataset
loan_data = pd.read_csv('/content/drive/MyDrive/loan_approval_dataset.csv')

# Define objective function (for demonstration, let's assume it's a simple function)
def objective_function(solution, data):
    # Calculate objective value (for demonstration, let's assume a simple objective)
    selected_features = data.columns[solution == 1]
    # Here you would perform your model training and evaluation to get accuracy
    # For demonstration, let's assume we calculate accuracy based on a dummy condition
    accuracy = np.sum(data[' loan_status'] == 1) / len(data)
    return accuracy

# Tabu Search Algorithm
def tabu_search(data, max_iter, tabu_size):
    best_solution = np.zeros(len(data.columns))  # Initial solution
    best_accuracy = objective_function(best_solution, data)  # Initial accuracy
    tabu_list = []  # Tabu list to store recent moves

    for _ in range(max_iter):
        neighbors = []  # List to store neighbor solutions
        for i in range(len(data.columns)):
            neighbor = best_solution.copy()
            neighbor[i] = 1 - neighbor[i]  # Flip the bit (feature)
            neighbors.append((neighbor, objective_function(neighbor, data)))

        # Select the best neighbor not in the tabu list
        sorted_neighbors = sorted(neighbors, key=lambda x: x[1], reverse=True)
        best_neighbor = None
        for neighbor, _ in sorted_neighbors:
            if neighbor.tolist() not in tabu_list:
                best_neighbor = neighbor
                break

        # Update best solution if a better neighbor is found
        if best_neighbor is not None:
            best_solution = best_neighbor
            best_accuracy = objective_function(best_solution, data)

        # Add the best solution to the tabu list
        tabu_list.append(best_solution.tolist())
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)  # Remove oldest move from tabu list

    return best_solution, best_accuracy

# Main
if __name__ == "__main__":
    # Define parameters
    max_iter = 100  # Maximum iterations
    tabu_size = 10  # Tabu list size

    # Run Tabu Search algorithm
    best_solution, best_accuracy = tabu_search(loan_data, max_iter, tabu_size)

    # Print results
    print("Best solution:", best_solution)
    print(f"Accuracy: {accuracy}")
    confusion = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Classification Report:\n{report}")
    correlation_matrix = np.corrcoef(y_test, y_pred)
    print("Correlation matrix:\n",correlation_matrix)
    cm=confusion_matrix(y_test,y_pred)
    z7=ConfusionMatrixDisplay(cm).plot()
    print("Confusion matrix:\n",cm)

import matplotlib.pyplot as plt

# Define the names of the models
models = ['Random Forest    ', '  Logistic Regression', '       SVM', 'KNN', 'Decision Tree  ', 'Tabu Search']

# Define the accuracies of the models (replace these with actual accuracies)
accuracies = [0.97, 0.90, 0.93, 0.87, 0.97, 0.98]

# Create a bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(models, accuracies, color='blue')

# Add labels above each bar
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01, f'{accuracy:.2f}', ha='center', va='bottom')

# Add labels and title
plt.xlabel('Models')
plt.ylabel('Accuracies')
plt.title('Accuracy of Different Models')
plt.ylim(0.5, 1.0)

# Show the plot
plt.show()

