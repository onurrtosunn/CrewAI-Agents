from __future__ import annotations

from typing import Optional
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

from .config.settings import settings

class MemoryFactory:
    @staticmethod
    def create_long_term_memory() -> LongTermMemory:
        return LongTermMemory(
            storage=LTMSQLiteStorage(
                db_path=settings.ltm_db_path
            )
        )

    @staticmethod
    def _build_rag_storage() -> RAGStorage:
        return RAGStorage(
            embedder_config={
                "provider": settings.embedding_provider,
                "config": {
                    "model": settings.embedding_model
                }
            },
            type="short_term",
            path=settings.memory_path
        )

    @staticmethod
    def create_short_term_memory() -> Optional[ShortTermMemory]:
        if not settings.enable_memory or settings.embedding_provider == "openai" and not settings.openai_api_key:
            return None
        return ShortTermMemory(storage=MemoryFactory._build_rag_storage())

    @staticmethod
    def create_entity_memory() -> Optional[EntityMemory]:
        if not settings.enable_memory or settings.embedding_provider == "openai" and not settings.openai_api_key:
            return None
        return EntityMemory(storage=MemoryFactory._build_rag_storage()) 