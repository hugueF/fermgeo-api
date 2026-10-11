import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from datetime import datetime
from sqlalchemy import String, DateTime, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Annonce(Base):
    __tablename__ = "annonces"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    produit: Mapped[str] = mapped_column(String, nullable=False)
    quantite: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    lat: Mapped[float] = mapped_column(Float, nullable=True)
    long: Mapped[float] = mapped_column(Float, nullable=True)