import os
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    RESOURCES_FOLDER = "resources"
    DOCUMENTS_PATH = f"{RESOURCES_FOLDER}/docs"
    CHROMA_PATH = f"{RESOURCES_FOLDER}/chroma"


settings = Settings()