import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from chroma_db import get_chroma_db

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


def query_rag(question):
    db = get_chroma_db()
    retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.5, "k": 3})
    docs = retriever.invoke(question)

    def format_docs(docs):
        return "\n\n ********* \n\n".join([d.page_content for d in docs])

    context = format_docs(docs)

    prompt_template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """

    prompt = prompt_template.format(context=context, question=question)
    llm = ChatOpenAI(model_name="gpt-4o-2024-08-06", temperature=0)
    result = llm.invoke(prompt)
    print(result.usage_metadata)
    return result.content


def query_chroma(question: str):
    db = get_chroma_db()
    collection = db._collection
    import chromadb.utils.embedding_functions as embedding_functions
    collection._embedding_function = embedding_functions.OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key=openai_api_key)
    results = collection.query(
        query_texts=question,
        n_results=3
    )
    return results


if __name__ == "__main__":
    query = "what's localstack"
    result = query_rag(query)
    # query_chroma(query)
    print(result)