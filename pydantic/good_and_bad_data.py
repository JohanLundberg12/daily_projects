from typing import Any
from pydantic import BaseModel, ValidationError


class Data(BaseModel):
    name: str
    age: int
    is_student: bool


def validate_data(data: dict[str, Any]) -> None:
    try:
        data = Data.model_validate(data)
        print(data)
    except ValidationError as e:
        print(f"data {data} is invalid")
        for error in e.errors():
            print(error)


def main():
    goood_data = {"name": "John", "age": 25, "is_student": True}
    bad_data = {"name": "", "age": {}, "is_student": "Tru"}

    validate_data(goood_data)
    validate_data(bad_data)


if __name__ == "__main__":
    main()
