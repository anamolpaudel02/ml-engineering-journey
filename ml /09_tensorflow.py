
from data_utils import load_data, prepare_data
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = load_data()
X_train, y_train, X_valid, y_valid, X_test, y_test = prepare_data(df)


def train_model(X_train, y_train, num_nodes, dropout_prob, lr, batch_size, epochs):
    nn_model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(10,)),
        tf.keras.layers.Dense(num_nodes, activation="relu"),
        tf.keras.layers.Dropout(dropout_prob),
        tf.keras.layers.Dense(num_nodes, activation="relu"),
        tf.keras.layers.Dropout(dropout_prob),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    nn_model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    history = nn_model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        verbose=0
    )

    return nn_model, history


least_val_loss = float("inf")
least_loss_model = None
least_params = None

epochs = 100

for num_nodes in [16, 32, 64]:
    for dropout_prob in [0, 0.2]:
        for lr in [0.01, 0.005, 0.001]:
            for batch_size in [32, 64, 128]:

                print(f"{num_nodes} nodes, dropout {dropout_prob}, lr {lr}, batch size {batch_size}")

                model, history = train_model(
                    X_train, y_train,
                    num_nodes, dropout_prob, lr, batch_size, epochs
                )

                val_loss = model.evaluate(X_valid, y_valid, verbose=0)[0]

                if val_loss < least_val_loss:
                    least_val_loss = val_loss
                    least_loss_model = model
                    least_params = (num_nodes, dropout_prob, lr, batch_size)


print("\nBest parameters:", least_params)
print("Best validation loss:", least_val_loss)


# Final evaluation on test data
probabilities = least_loss_model.predict(X_test, verbose=0).flatten()
predictions = (probabilities >= 0.5).astype(int)

print("\nTest Results:")
print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1-score:", f1_score(y_test, predictions))
