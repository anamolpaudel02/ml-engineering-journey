
from data_utils import load_data, prepare_data
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = load_data()
X_train, y_train, X_valid, y_valid, X_test, y_test = prepare_data(df)

model = GaussianNB()
model.fit(X_train, y_train)

predictions = model.predict(X_valid)
print("Validation accuracy:", accuracy_score(y_valid, predictions))
print("Precision:", precision_score(y_valid, predictions))
print("Recall:", recall_score(y_valid, predictions))
print("F1-score:", f1_score(y_valid, predictions))