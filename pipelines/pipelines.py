import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __():
    from sklearn.datasets import fetch_openml
    from sklearn.pipeline import Pipeline, make_pipeline, make_union
    from sklearn.preprocessing import OneHotEncoder, Binarizer
    from sklearn.impute import SimpleImputer
    from skrub import SelectCols
    from sklearn.ensemble import HistGradientBoostingClassifier

    return (
        Binarizer,
        HistGradientBoostingClassifier,
        OneHotEncoder,
        Pipeline,
        SelectCols,
        SimpleImputer,
        fetch_openml,
        make_pipeline,
        make_union,
    )


@app.cell
def __(fetch_openml):
    X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
    return X, y


@app.cell
def __(X):
    X
    return


@app.cell
def __(OneHotEncoder, Pipeline, SelectCols):
    # using "Pipeline" we can specify the naming of each step

    pipe = Pipeline([
        ("pclass_col", SelectCols("pclass")),
        ("pclass_enc", OneHotEncoder(sparse_output=False))
    ])
    pipe.get_params()
    return pipe,


@app.cell
def __(OneHotEncoder, SelectCols, make_pipeline):
    # using make_pipeline the names of the steps will be inferred from the method, i.e. lower case of SelectCols: selectcols__name etc.

    pipe1 = make_pipeline(
        SelectCols("pclass"),
        OneHotEncoder()
    )
    pipe1.get_params()
    return pipe1,


@app.cell
def __(OneHotEncoder, SelectCols, make_pipeline, make_union):
    pipe2 = make_union(
        make_pipeline(
            SelectCols("pclass"),
            OneHotEncoder(sparse_output=False)
        ),
        SelectCols("age")
    )
    pipe2
    return pipe2,


@app.cell
def __(HistGradientBoostingClassifier, make_pipeline, pipe2):
    feat_pipe = pipe2
    main_pipe = make_pipeline(
        feat_pipe,
        HistGradientBoostingClassifier()
    )
    main_pipe
    return feat_pipe, main_pipe


@app.cell
def __(
    Binarizer,
    OneHotEncoder,
    SelectCols,
    SimpleImputer,
    make_pipeline,
    make_union,
):
    # imputing missing age values and simply assuming that
    # you are not a child
    # Then: 
    # age -> pipe -> impute missing 
    # -> make two new features indicating less than 18 and less than 12. These are then concatenated

    feat_pipe2 = make_union(
        make_pipeline(
            SelectCols("pclass"),
            OneHotEncoder(sparse_output=False)
        ),
        make_pipeline(
            SelectCols("sex"),
            OneHotEncoder(sparse_output=False)
        ),
        make_pipeline(
            SelectCols("age"),
            SimpleImputer(fill_value=19, strategy="constant"),
            make_union(
                Binarizer(threshold=18),
                Binarizer(threshold=12)
            )
        ),
        SelectCols(["fare", "age"])
    )
    feat_pipe2
    return feat_pipe2,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
