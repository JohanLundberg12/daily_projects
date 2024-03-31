import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    from sklearn.datasets import fetch_openml
    from sklearn.impute import SimpleImputer
    from skrub import SelectCols
    from sklearn.preprocessing import OneHotEncoder, Binarizer
    from sklearn.pipeline import make_pipeline, make_union
    from sklearn.compose import ColumnTransformer, make_column_transformer, make_column_selector
    return (
        Binarizer,
        ColumnTransformer,
        OneHotEncoder,
        SelectCols,
        SimpleImputer,
        fetch_openml,
        make_column_selector,
        make_column_transformer,
        make_pipeline,
        make_union,
        np,
    )


@app.cell
def __(fetch_openml):
    X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    return X, y


@app.cell
def __(
    Binarizer,
    ColumnTransformer,
    OneHotEncoder,
    SimpleImputer,
    make_column_transformer,
    make_pipeline,
    make_union,
):
    age_pipe = make_pipeline(
        SimpleImputer(fill_value=19, strategy="constant"),
        make_union(
            Binarizer(threshold=18),
            Binarizer(threshold=12)
        )
    )

    feat_pipe = ColumnTransformer([
        ("one_hot_features", OneHotEncoder(), ["pclass", "sex"]),
        ("age_binary", age_pipe, ["age"]),
        ("given_features"), "passthrough", ["fare", "age"]
    ])

    # names generated automatically
    feat_pipe_alt = make_column_transformer(
        (OneHotEncoder(), ["pclass", "sex"]),
        (age_pipe, ["age"]),
        ("passthrough", ["fare", "age"])
    )
    feat_pipe
    return age_pipe, feat_pipe, feat_pipe_alt


@app.cell
def __(feat_pipe_alt):
    feat_pipe_alt
    return


@app.cell
def __(X, make_column_selector, make_column_transformer, np):
    # select columns for the transformer based on the dtype

    detect_numerical_cols = make_column_selector(dtype_include=np.number)
    detect_non_numerical_cols = make_column_selector(dtype_exclude=np.number)

    auto_col_select_pipe = make_column_transformer(
        ("passthrough", detect_non_numerical_cols)
    ).fit_transform(X)
    print(auto_col_select_pipe)

    auto_col_select_pipe = make_column_transformer(
        ("passthrough", detect_numerical_cols)
    ).fit_transform(X)

    print(auto_col_select_pipe)
    return (
        auto_col_select_pipe,
        detect_non_numerical_cols,
        detect_numerical_cols,
    )


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
