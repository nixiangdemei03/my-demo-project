"""Product model"""
import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import String, Integer, Text, DateTime, ForeignKey, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    supplier_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    category_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False)
    name_zh: Mapped[str] = mapped_column(String(255), nullable=False)
    name_en: Mapped[str] = mapped_column(String(255), nullable=True)
    oem_number: Mapped[str] = mapped_column(String(100), nullable=True)
    description_zh: Mapped[str] = mapped_column(Text, nullable=True)
    description_en: Mapped[str] = mapped_column(Text, nullable=True)
    original_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=True)  # CNY
    sell_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)      # USD
    moq: Mapped[int] = mapped_column(Integer, default=1)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    specs: Mapped[dict] = mapped_column(JSONB, default=dict)
    warranty: Mapped[str] = mapped_column(String(200), nullable=True)
    return_policy: Mapped[str] = mapped_column(String(200), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="active")  # active / inactive / deleted
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
