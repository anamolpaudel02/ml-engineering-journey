
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

def load_data():
    columns = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
    df = pd.read_csv(
        "/Users/anamolpaudel/Downloads/python/ml /magic04.data",
        names=columns
    )

    df["class"] = (df["class"] == "g").astype(int)
    print(df["class"].unique())

    return df


def prepare_data(df):
    train, valid, test = np.split(
        df.sample(frac=1, random_state=42).to_numpy(),
        [int(0.6 * len(df)), int(0.8 * len(df))]
    )

    def scale_dataset(dataframe, oversample=False):
        x = dataframe[:, :-1]
        y = dataframe[:, -1]

        scaler = StandardScaler()
        x = scaler.fit_transform(x)

        if oversample:
            ros = RandomOverSampler()
            x, y = ros.fit_resample(x, y)

        data = np.hstack((x, np.reshape(y, (-1, 1))))
        return data, x, y

    # letsknow how many dataset are there for gammas and handrons
    print(len(train[train[:, -1] == 1]))
    print(len(train[train[:, -1] == 0]))

    train, X_train, y_train = scale_dataset(train, oversample=True)
    valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
    test, X_test, y_test = scale_dataset(test, oversample=False)

    # # lets check if the values are same or not  : which are exactly equal
    # print(sum(y_train ==1))
    # print(sum(y_train ==0))

    return X_train, y_train, X_valid, y_valid, X_test, y_test
