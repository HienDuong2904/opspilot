from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/identity_db"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
