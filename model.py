# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# Step 1: Load the dataset
dataset = pd.read_csv("student_data.csv")


# Step 2: Separate input features and output label
features = dataset.drop("result", axis=1)
target = dataset["result"]


# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)


# Step 4: Create and train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# Step 5: Make predictions on test data
predictions = model.predict(X_test)


# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("\nModel Evaluation:")
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)


# Step 7: Test with a new sample input (likely poor performance)
new_student1 = pd.DataFrame(
    [[4, 65, 5, 6, 60, 70, 8]],
    columns=features.columns
)

result = model.predict(new_student1)

print("\nPrediction for New student 1:")
print("0 = Poor Performance, 1 = Good Performance")
print("Predicted Result:", result[0])


# Step 8: Test with another sample input (likely good performance)
new_student2 = pd.DataFrame(
    [[8, 90, 7, 2, 88, 92, 2]],
    columns=features.columns
)

result2 = model.predict(new_student2)

print("\nPrediction for New student 2:")
print("0 = Poor Performance, 1 = Good Performance")
print("Predicted Result:", result2[0])