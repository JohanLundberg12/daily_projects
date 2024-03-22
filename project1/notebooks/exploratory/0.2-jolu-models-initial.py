import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __():
    import pandas as pd
    import lazypredict as lp
    from lazypredict.Supervised import LazyClassifier

    import torch, torch.nn as nn
    from skorch import NeuralNetClassifier
    return LazyClassifier, NeuralNetClassifier, lp, nn, pd, torch


@app.cell
def __(pd):
    data = pd.read_csv("data/processed/car_evaluation_encoded.csv")
    return data,


@app.cell
def __(data):
    data.shape
    return


@app.cell
def __(data):
    df = data.sample(frac=1)
    return df,


@app.cell
def __(df):
    offset = int(len(df) * 0.9)
    train = df.iloc[:offset]
    test = df.iloc[offset:]

    X_train = train.drop(columns=train.columns[-1])
    y_train = train["evaluation_level"]

    X_test = test.drop(columns=test.columns[-1])
    y_test = test["evaluation_level"]
    return X_test, X_train, offset, test, train, y_test, y_train


@app.cell
def __(X_train, y_train):
    y_train.shape, X_train.shape
    return


@app.cell
def __(LazyClassifier):
    clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
    return clf,


@app.cell
def __(clf):
    clf
    return


@app.cell
def __(X_test, X_train, clf, y_test, y_train):
    models,predictions = clf.fit(X_train, X_test, y_train, y_test)
    return models, predictions


@app.cell
def __(models):
    models
    return


@app.cell
def __(X_train, torch, y_train):
    X_train_tensor = torch.tensor(X_train.values).float()
    y_train_tensor = torch.tensor(y_train.values)
    return X_train_tensor, y_train_tensor


@app.cell
def __(NeuralNetClassifier, nn, torch):
    class MyClassifier(nn.Module):
        def __init__(self):
            super(MyClassifier, self).__init__()
            self.fc1 = nn.Linear(6, 6)
            self.fc2 = nn.Linear(6, 4)

            self.sequential = nn.Sequential(
                self.fc1,
                nn.ReLU(),
                self.fc2
            )

        def forward(self, x):
            return self.sequential(x)

    model = NeuralNetClassifier(
        MyClassifier,
        lr=0.01,
        criterion=nn.CrossEntropyLoss,
        batch_size=4,
        optimizer=torch.optim.Adam
    )
    return MyClassifier, model


@app.cell
def __(X_train_tensor, model, y_train_tensor):
    model.fit(X_train_tensor, y_train_tensor)
    return


@app.cell
def __(X_test, torch, y_test):
    X_test_tensor = torch.tensor(X_test.values).float()
    y_test_tensor = torch.tensor(y_test.values)
    return X_test_tensor, y_test_tensor


@app.cell
def __(X_test_tensor, model):
    model.predict(X_test_tensor)
    return


@app.cell
def __(X_test_tensor, model, y_test_tensor):
    model.score(X_test_tensor, y_test_tensor)
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
