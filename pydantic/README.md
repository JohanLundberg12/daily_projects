### Pydantic Use Cases

1. We can validate the format of a field using the @pydantic.field_validator decorator.
2. We can validate whether a field is present or not using the @pydantic.model_validator decorator.
3. We can easily make a field immutable by defining a Config class with frozen=True, inside a class for a data object.
4. Similar to 3, we can easily change whether a field is in lower case when we print it with str_to_lower=True.
