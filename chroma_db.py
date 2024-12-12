from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from config import settings

_db_instance = None


def get_chroma_db():
    global _db_instance
    if _db_instance is None:
        embeddings = OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)
        _db_instance = Chroma(
            persist_directory=str(settings.CHROMA_PATH),
            embedding_function=embeddings
        )
    return _db_instance
