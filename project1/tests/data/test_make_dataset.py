import pandas as pd


def test_encode_ordinal_variables():
    from src.data.make_dataset import encode_ordinal_variables

    df = pd.DataFrame(
        {
            "buying_price": ["vhigh", "high", "med", "low"],
            "maint_price": ["vhigh", "high", "med", "low"],
            "luggage_boot_size": ["big", "med", "small", "big"],
            "safety_estimate": ["high", "med", "low", "high"],
            "num_doors": ["2", "4", "4", "2"],
            "capacity_pers": ["2", "4", "more", "more"],
        }
    )
    df_encoded = encode_ordinal_variables(df, "src/data/mappings.json")

    for column in df:
        assert df_encoded[column].dtype == "int64"


if __name__ == "__main__":
    test_encode_ordinal_variables()
