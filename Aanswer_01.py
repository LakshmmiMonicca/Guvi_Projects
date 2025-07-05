import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load training data
train = pd.read_csv("/data/training/train.csv")

# Step 2: Map string price labels to integers
label_map = {'Low tier': 0, 'Medium tier': 1, 'High tier': 2, 'Expensive tier': 3}
train['price_range'] = train['price_range'].map(label_map)

# Step 3: Prepare training features and target
X = train.drop(columns=['id', 'price_range'])
y = train['price_range']

# Step 4: Optional validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train better RandomForest model
model = RandomForestClassifier(
    n_estimators=300,       # More trees
    max_depth=15,           # Limit depth to prevent overfitting
    min_samples_split=4,    # Better generalization
    random_state=42
)
model.fit(X_train, y_train)

# Step 6: Evaluate on validation set
val_preds = model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_preds)
print("Validation Accuracy:", val_accuracy)

# Step 7: Load test set
test = pd.read_csv("/data/test/test.csv")
test_ids = test['id']
X_test = test.drop(columns=['id'])

# Step 8: Predict
test_preds = model.predict(X_test)

# Step 9: Reverse map predictions to string labels
reverse_map = {0: 'Low tier', 1: 'Medium tier', 2: 'High tier', 3: 'Expensive tier'}
test_preds_labels = [reverse_map[p] for p in test_preds]

# Step 10: Save final output
output = pd.DataFrame({
    'id': test_ids,
    'price_range': test_preds_labels
})
output.to_csv("/code/prediction.csv", index=False, encoding='utf-8')
