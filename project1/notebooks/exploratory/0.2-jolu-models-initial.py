import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __():
    import pandas as pd
    import lazypredict as lp
    from lazypredict.Supervised import LazyClassifier
    return LazyClassifier, lp, pd


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
def __():
    return


if __name__ == "__main__":
    app.run()
