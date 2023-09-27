from src.clients.qdrant import QClient
from src.clients.openai import OpenAIClient
from langchain.text_splitter import CharacterTextSplitter


class Embedder:
    vector_db_client = QClient()
    openai_client = OpenAIClient()

    def embed_information(self, collection: str, text: str):
        """Embeds information into the vector database

        Args:
            collection (str): Collection to store the information
            text (str): Information to embed
        """
        self.vector_db_client.recreate_collection(collection=collection)
        text_chunks = CharacterTextSplitter().split_text(text)
        index = 0
        vectors: list[tuple[int, list[float], dict]] = []
        for text_chunk in text_chunks:
            embedding = self.openai_client.create_embedding(text_chunk)
            vectors.append((index, embedding, {"content": text_chunk}))

        self.vector_db_client.upsert_many(
            collection=collection,
            vectors=vectors,
        )
