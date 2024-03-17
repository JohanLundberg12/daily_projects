from pydantic import BaseModel, Field


class ColumnMapping(BaseModel):
    col: str
    mapping: dict[str, int] = Field(
        ..., description="Mapping of text values to numerical values"
    )


class EncoderMappings(BaseModel):
    mappings: list[ColumnMapping]
