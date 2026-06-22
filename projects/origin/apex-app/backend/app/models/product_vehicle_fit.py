"""ProductVehicleFit — vehicle compatibility matching"""
import uuid
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class ProductVehicleFit(Base):
    __tablename__ = "product_vehicle_fits"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    make: Mapped[str] = mapped_column(String(100), nullable=False)  # e.g., Toyota
    model: Mapped[str] = mapped_column(String(100), nullable=False)  # e.g., Hilux
    year_start: Mapped[int] = mapped_column(Integer, nullable=False)
    year_end: Mapped[int] = mapped_column(Integer, nullable=False)
    engine: Mapped[str] = mapped_column(String(100), nullable=True)  # e.g., 1GD-FTV
    vin_pattern: Mapped[str] = mapped_column(String(50), nullable=True)  # e.g., MR0*
