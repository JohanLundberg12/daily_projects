from collections import defaultdict
from typing import List

import pyodbc


class DatabaseError(Exception):
    """Custom exception for database-related errors."""

    pass


def connect_to_database(server: str, database: str) -> pyodbc.Connection:
    """Creates and returns a database connection.

    Args:
        server: The database server name or address.
        database: The database name.

    Returns:
        An active pyodbc connection object.

    Raises:
        DatabaseError: If an error occurs during connection.
    """

    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        raise DatabaseError(f"Database connection error: {e}") from e


def retrieve_schemas(cursor: pyodbc.Cursor, include_views: bool = True) -> List[str]:
    """Retrieves a list of schemas from the database.

    Args:
        cursor: An active pyodbc cursor object.
        include_views: If True, includes views in the results.

    Returns:
        A list of schema names.
    """

    method = "views" if include_views else "tables"
    query = f"SELECT DISTINCT schema_name(schema_id) as schema_ FROM sys.{method}"
    schemas: list[pyodbc.Row] = cursor.execute(query).fetchall()

    return [schema[0] for schema in schemas]


def fetch_tables(cursor: pyodbc.Cursor, schemas: List[str]) -> List[List[str]]:
    """Retrieves tables from the specified schemas.

    Args:
        cursor: An active pyodbc cursor object.
        schemas: A list of schema names.

    Returns:
        A nested list of tables (grouped by schema).
    """
    try:
        return [
            [row.table_name for row in cursor.tables(schema=schema, tableType="VIEW")]
            for schema in schemas
        ]
    except pyodbc.Error as e:
        print(e)
        raise


def get_database_columns(cursor: pyodbc.Cursor, schema: str, table: str) -> list[str]:
    """Return a list of columns in the table"""
    try:
        columns = [
            row.column_name for row in cursor.columns(table=table, schema=schema)
        ]
        return columns
    except pyodbc.Error as e:
        print(e)
        raise


def create_database_tables_columns_dict(server, database, views=True):
    """Return a dictionary containing the tables and columns in the database

    The dictionary is structured as follows:
    {
        "schema1": {
            "table1": ["column1", "column2", ...],
            "table2": ["column1", "column2", ...],
            ...
        },
        "schema2": {
            "table1": ["column1", "column2", ...],
            "table2": ["column1", "column2", ...],
            ...
        },
        ...
    }
    """
    connection = create_database_connection(server, database)
    cursor = connection.cursor()

    schemas = get_schemas(cursor, views)
    tables = get_database_tables(cursor, schemas)

    tables_columns_dict = defaultdict(dict)
    for schema, schema_tables in zip(schemas, tables):
        for table in schema_tables:
            columns = get_database_columns(cursor, schema, table)
            tables_columns_dict[schema][table] = columns

    return tables_columns_dict


def _create_node(
    id_counter: iter, node_type: str, node_name: str, node_parent: str
) -> dict:
    """Create a node dictionary.

    We call next(id_counter) inside the function to
    have it take care of generating the ID for each node."""

    colour_map = {
        "database": "black",
        "schema": "orange",
        "table": "green",
        "column": "blue",
    }
    colour = colour_map[node_type]

    return {
        "id": next(id_counter),
        "type": node_type,
        "name": node_name,
        "parent": node_parent,
        "colour": colour,
    }


def create_schema_structure(database, schemas) -> dict:
    """An example of the structure of the dictionary:

    {
        "id": 1,
        "type": "database",
        "name": "Adventure",
        "parent": None,
        "nodes": {
            "id": 2,
            "type": "schema",
            "name": "sales",
            "parent": "Adventure",
            "nodes": {
                "id": 3,
                "type": "table",
                "name": "orders",
                "parent": "sales",
                "nodes": {
                    "id": 4,
                    "type": "column",
                    "name": "order_id",
                    "parent": "orders",
                }
            }
        }
    }
    """

    id_counter = iter(range(1, 1 << 30))

    database = _create_node(id_counter, "database", database, None)

    for schema_name, tables in schemas.items():
        schema = _create_node(id_counter, "schema", schema_name, database)

        for table, columns in tables.items():
            table = _create_node(id_counter, "table", table, schema)

            for column in columns:
                column = _create_node(id_counter, "column", column, table)

                table["nodes"][column] = column

            schema["nodes"][table] = table

        database["nodes"][schema] = schema

    return database
