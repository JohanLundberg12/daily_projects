# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import category_encoders as ec
import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv

from src.data.mappings import EncoderMappings


def encode_ordinal_variables(df: pd.DataFrame, mappings_file: str) -> pd.DataFrame:
    """Encode ordinal variables in a dataframe using a json mappings file.

    Args:
        df (pd.DataFrame): The dataframe to encode.
        mappings_file (str): The path to the mappings file.

    Returns:
        pd.DataFrame: The encoded dataframe.
    """

    with open(mappings_file, "r") as file:
        mappings_data = file.read()
    mappings = EncoderMappings.parse_raw(mappings_data)
    mappings = [mapping.dict() for mapping in mappings.mappings]
    encoder = ec.OrdinalEncoder(mapping=mappings, return_df=True)
    df_encoded = encoder.fit_transform(df)

    return df_encoded


def label_encoder(df: pd.DataFrame, col) -> pd.DataFrame:
    from sklearn.preprocessing import LabelEncoder

    label_encoder = LabelEncoder()
    df[col] = label_encoder.fit_transform(df[col])
    return df


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making interim data set from raw data")

    df = pd.read_csv(input_filepath)
    df.columns = [
        "buying_price",
        "maint_price",
        "num_doors",
        "capacity_pers",
        "luggage_boot_size",
        "safety_estimate",
        "evaluation_level",
    ]
    df_encoded = encode_ordinal_variables(df, "src/data/mappings.json")
    df_encoded = label_encoder(df_encoded, "evaluation_level")
    df_encoded.to_csv(output_filepath, index=False)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
