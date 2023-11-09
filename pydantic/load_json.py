import json
from typing import Optional, List
import pydantic


class ISBNCodeFormatError(Exception):
    """Custom error that is raised when ISBN code is not valid"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Movie(pydantic.BaseModel):
    title: str
    author: str
    publication_year: int
    price: float
    isbn_code: Optional[str]

    @pydantic.field_validator("isbn_code")
    @classmethod
    def isbn_code_valid(cls, value):
        """Validator to validate whether ISBNCode is valid."""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBNCodeFormatError(
                value=value, message="ISBN code must be 10 characters long"
            )

        def get_weighted_sum(chars: str) -> int:
            def calc_weight(i: int, x: str) -> int:
                return (10 - i) * char_to_int(x)

            def char_to_int(char: str) -> int:
                if char in "Xx":
                    return 10
                return int(char)

            return sum(calc_weight(i, x) for i, x in enumerate(chars))

        weighted_sum = get_weighted_sum(chars)

        if weighted_sum % 11 != 0:
            MSG = "ISNBCode digit sum should be divisible by 11"
            raise ISBNCodeFormatError(value=value, message=MSG)

        return value


# Load the JSON file into a variable
with open("json.json") as f:
    data = json.load(f)
    movies: List[Movie] = [Movie(**movie) for movie in data]
    print(movies)
