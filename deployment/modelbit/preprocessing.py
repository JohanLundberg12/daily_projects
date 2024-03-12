from sklearn.preprocessing import StandardScaler


def preprocess_data(data):
    # the input data is a list of list of 30 numbers. normalise them
    # using sklearn

    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)
    return data
