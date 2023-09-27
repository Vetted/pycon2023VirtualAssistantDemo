from src.clients.qdrant import QClient
from src.clients.openai import OpenAIClient
from src.constants import DEMO_COLLECTION_NAME, QNA_PROMPT


class Assistant:
    vector_db_client = QClient()
    llm_client = OpenAIClient()

    def get_answer(self, question: str) -> str:
        """Answers to user provided question

        Args:
            question (str): Question to answer

        Returns:
            str: Answer to the question
        """
        question_embedding = self.llm_client.create_embedding(question)
        relevant_contexts = self.vector_db_client.query(
            collection=DEMO_COLLECTION_NAME,
            query_embedding=question_embedding,
            top_n=5,
        )
        context_items = [item[2]["content"] for item in relevant_contexts]
        prompt = QNA_PROMPT.format(
            question=question, context="\n\n".join(context_items)
        )
        msgs = [{"role": "user", "content": prompt}]
        answer = self.llm_client.create_chat_completion(messages=msgs)
        return answer
