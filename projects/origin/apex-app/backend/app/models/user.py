"""User model — supplier / buyer / admin"""
import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="buyer")  # supplier / buyer / admin
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    contact_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    country: Mapped[str] = mapped_column(String(100), nullable=True)
    language: Mapped[str] = mapped_column(String(10), default="zh")
    verified: Mapped[bool] = mapped_column(Boolean, default=False)
    # Supplier profile fields (Issue 08)
    logo_url: Mapped[str] = mapped_column(String(500), nullable=True)
    established_year: Mapped[int] = mapped_column(nullable=True)
    main_brands: Mapped[str] = mapped_column(String(500), nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(String(500), nullable=True)
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
