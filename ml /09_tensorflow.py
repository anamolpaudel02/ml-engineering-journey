
from data_utils import load_data, prepare_data
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = load_data()
X_train, y_train, X_valid, y_valid, X_test, y_test = prepare_data(df)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(10,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_valid, y_valid)
)

probabilities = model.predict(X_valid).flatten()
predictions = (probabilities >= 0.5).astype(int)

print("Accuracy:", accuracy_score(y_valid, predictions))
print("Precision:", precision_score(y_valid, predictions))
print("Recall:", recall_score(y_valid, predictions))
print("F1-score:", f1_score(y_valid, predictions))
 