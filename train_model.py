
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create and train the AI model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the trained model
joblib.dump(model, "model.pkl")

print("AI Model trained successfully!")
print("Model saved as model.pkl")
