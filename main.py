import os
from src.embedder import Embedder
from src.assistant import Assistant
from src.constants import DEMO_COLLECTION_NAME


def index_documents():
    # read all text files in the documents folder

    for file_name in os.listdir("./documents"):
        with open(f"./documents/{file_name}", "r") as f:
            text = f.read()

        print(f"Indexing document: {file_name}")
        Embedder().embed_information(
            collection=DEMO_COLLECTION_NAME,
            text=text,
            name=file_name,
        )


def query_documents():
    while True:
        question = input("Ask a question, Type 'exit' to exit: ")
        if question.lower().strip() == "exit":
            break

        answer = Assistant().get_answer(question=question)
        print(f"Answer: {answer}")
        print("\n\n\n")


def main():
    # index_documents()
    query_documents()


if __name__ == "__main__":
    main()
