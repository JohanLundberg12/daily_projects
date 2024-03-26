# parquet files are generally more efficent compared to csv
import logging
from pathlib import Path

import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv


def load_csv_to_parquet(csv_path, parquet_path):
    """_summary_
    Load csv file and save it as a parquet file.
    """
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path)

    print("CSV file loaded to parquet file.")


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath, output_filepath):
    logger = logging.getLogger(__name__)
    logger.info("making interim data set from raw data")

    load_csv_to_parquet(input_filepath, output_filepath)

    logger.info("interim data set created")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
