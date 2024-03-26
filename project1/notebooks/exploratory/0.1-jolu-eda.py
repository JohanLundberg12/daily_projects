import marimo

__generated_with = "0.3.3"
app = marimo.App()


@app.cell
def __(__file__):
    import dotenv
    import os
    from pathlib import Path

    path = os.path.dirname(__file__)
    dotenv_path = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_path)

    source_dir = os.path.dirname(dotenv_path)
    return Path, dotenv, dotenv_path, os, path, source_dir


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import pandas as pd

    import seaborn as sns


    import itables
    import sidetable
    import skimpy as skim
    from summarytools import dfSummary

    from ydata_profiling import ProfileReport
    return (
        ProfileReport,
        dfSummary,
        itables,
        mo,
        np,
        pd,
        sidetable,
        skim,
        sns,
    )


@app.cell
def __(pd):
    file = "data/interim/car_evaluation.parquet"
    df = pd.read_parquet(file)
    return df, file


@app.cell
def __(df):
    df
    return


@app.cell
def __(df, skim):
    skim.skim(df)
    return


@app.cell
def __(df, dfSummary):
    dfSummary(df)
    return


@app.cell
def __(ProfileReport, df, source_dir):
    report = ProfileReport(df)
    report.to_file(source_dir + "./notebooks/reports/01-jolu-eda.html")
    return report,


@app.cell
def __(df):
    df.head(1)
    return


@app.cell
def __(df):
    df.columns = ["buying_price", "maint_price", "num_doors", "capacity_pers", "luggage_boot_size", "safety_estimate", "evaluation_level"]
    return


@app.cell
def __():
    from src.data import make_dataset
    return make_dataset,


@app.cell
def __(df, make_dataset):
    df1 = make_dataset.encode_ordinal_variables(df, "src/data/mappings.json")
    df1 = make_dataset.label_encoder(df1, "evaluation_level")
    return df1,


@app.cell
def __(df1):
    df1.head(2)
    return


@app.cell
def __(df1, skim):
    skim.skim(df1)
    return


@app.cell
def __(df1):
    df1
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
