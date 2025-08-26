from __future__ import annotations

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # LLM provider/model
    llm_provider: str = Field(default=os.getenv("LLM_PROVIDER", "openai"))
    llm_model_manager: str = Field(default=os.getenv("LLM_MODEL_MANAGER", "openai/gpt-4o"))
    llm_model_default: str = Field(default=os.getenv("LLM_MODEL_DEFAULT", "openai/gpt-4o-mini"))

    # OpenAI
    openai_api_key: str | None = Field(default=os.getenv("OPENAI_API_KEY"))
    openai_org: str | None = Field(default=os.getenv("OPENAI_ORG"))
    openai_api_base: str | None = Field(default=os.getenv("OPENAI_API_BASE"))

    # Serper
    serper_api_key: str | None = Field(default=os.getenv("SERPER_API_KEY"))

    # Embeddings
    embedding_provider: str = Field(default=os.getenv("EMBEDDING_PROVIDER", "openai"))
    embedding_model: str = Field(default=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"))

    # Memory
    enable_memory: bool = Field(default=os.getenv("ENABLE_MEMORY", "true").lower() == "true")
    memory_path: str = Field(default=os.getenv("MEMORY_PATH", "./memory/"))
    ltm_db_path: str = Field(default=os.getenv("LTM_DB_PATH", "./memory/long_term_memory_storage.db"))

settings = AppSettings() 