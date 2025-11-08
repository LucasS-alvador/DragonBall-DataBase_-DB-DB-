from src.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date
from typing import List
from datetime import date

class Obra(db.Model):
    __tablename__ = "Obra"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False)
    dtIni: Mapped[date] = mapped_column(Date, nullable=False)
    dtFim: Mapped[date] = mapped_column(Date, nullable=False)
    imagem: Mapped[str] = mapped_column(String(256))

    sagas: Mapped[List["Saga"]] = db.relationship(
        "Saga", 
        back_populates="obra", 
        cascade="all, delete-orphan")