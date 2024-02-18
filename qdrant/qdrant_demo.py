from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)

# By default, Qdrant starts with no encryption or authentication .
# This means anyone with network access to your machine can access your Qdrant container instance.
# Please read Security https://qdrant.tech/documentation/quick-start/#:~:text=instance.%20Please%20read-,Security,-carefully%20for%20details
# carefully for details on how to secure your instance.

client = QdrantClient(":memory:")
collection_name = "test_collection"

# this collection uses cosine distance to compare vectors
client.create_collection(
    collection_name=f"{collection_name}",
    vectors_config=VectorParams(size=4, distance=Distance.COSINE),
)

operation_info = client.upsert(
    collection_name=f"{collection_name}",
    wait=True,
    points=[
        PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
        PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
        PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
        PointStruct(
            id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}
        ),
        PointStruct(id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}),
        PointStruct(id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}),
    ],
)

print(operation_info)

# query: which vector most similar to this one
search_result = client.search(
    collection_name=f"{collection_name}", query_vector=[0.2, 0.1, 0.9, 0.7], limit=3
)

print(search_result)


# query vector using payload infomation as filter
search_result = client.search(
    collection_name="test_collection",
    query_vector=[0.2, 0.1, 0.9, 0.7],
    query_filter=Filter(
        must=[FieldCondition(key="city", match=MatchValue(value="London"))]
    ),
    with_payload=True,
    limit=3,
)

print(search_result)
