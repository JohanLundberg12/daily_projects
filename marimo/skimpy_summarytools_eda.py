import marimo

__generated_with = "0.2.6"
app = marimo.App(width="full")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import sys
    import time
    import datetime
    import pickle
    import json
    import requests

    # import wine _data set or titanic
    from sklearn.datasets import load_wine

    from skimpy import skim, generate_test_data
    from summarytools import dfSummary
    return (
        datetime,
        dfSummary,
        generate_test_data,
        json,
        load_wine,
        mo,
        np,
        os,
        pd,
        pickle,
        plt,
        requests,
        skim,
        sns,
        sys,
        time,
    )


@app.cell
def __(load_wine):
    wine = load_wine()
    return wine,


@app.cell
def __(pd, wine):
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    return df,


@app.cell
def __(df):
    df
    return


@app.cell
def __(df, dfSummary):
    dfSummary(df)
    return


@app.cell
def __(df, skim):
    skim(df)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
