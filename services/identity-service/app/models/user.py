import uuid
from sqlalchemy import String, Column, Boolean, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func

from app.db.base import Base, TimestampMixin, UUIDMixin

class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )
    user_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )
    password: Mapped[str] = mapped_column(
        String(512),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
