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


class QdrantDemo:
    def __init__(self):
        self.client = QdrantClient(":memory:")

    def create_collection(self,  collection_name, vector_size, distance):
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=distance),
        )

    def upsert_points(self, collection_name, points):
        operation_info = self.client.upsert(
            collection_name=collection_name,
            wait=True,
            points=points,
        )
        print(operation_info)

    def search_vector(self, collection_name, query_vector, limit):
        search_result = self.client.search(
            collection_name=collection_name, query_vector=query_vector, limit=limit
        )
        print(search_result)

    def search_vector_with_filter(self, collection_name, query_vector, query_filter, limit):
        search_result = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            query_filter=query_filter,
            with_payload=True,
            limit=limit,
        )
        print(search_result)


if __name__ == "__main__":
    demo = QdrantDemo()
    collection_name = "example_collection"
    demo.create_collection(collection_name, vector_size=4, distance="Cosine")
    
    points = [
        PointStruct(
            id=1,
            vector=[0.2, 0.1, 0.9, 0.7],
            payload={"city": "London"}
        ),
        PointStruct(
            id=2,
            vector=[0.4, 0.1, 0.6, 0.8],
            payload={"city": "Berlin"}
        ),
        PointStruct(
            id=3,
            vector=[0.5, 0.2, 0.8, 0.9],
            payload={"city": "Paris"}
        )
    ]
    
    demo.upsert_points(collection_name, points)
    demo.search_vector(collection_name, query_vector=[0.3, 0.2, 0.9, 0.7], limit=2)
    query_filter = Filter(
        must=[FieldCondition(key="city", match=MatchValue(value="London"))]
    )
    demo.search_vector_with_filter(collection_name, query_vector=[0.3, 0.2, 0.9, 0.7], query_filter=query_filter, limit=1)
