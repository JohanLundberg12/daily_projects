from pydantic import BaseModel, Field


class ColumnMapping(BaseModel):
    """
    Column mapping for a single column.
    """

    col: str
    mapping: dict[str, int] = Field(
        ..., description="Mapping of text values to numerical values"
    )


class EncoderMappings(BaseModel):
    """
    Encoder mappings for all columns.
    """

    mappings: list[ColumnMapping]
