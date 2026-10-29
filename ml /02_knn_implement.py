
from data_utils import load_data, prepare_data
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = load_data()
X_train, y_train, X_valid, y_valid, X_test, y_test = prepare_data(df)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

predictions = model.predict(X_valid)
print("Validation accuracy:", accuracy_score(y_valid, predictions))
