from database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from typing import List

class Raca(db.Model):
    __tablename__ = "Raca"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    cor: Mapped[str] = mapped_column(String(64))
    desc: Mapped[str] = mapped_column(String(1024))
    poderBase: Mapped[int] = mapped_column(db.Integer, nullable=False)    
    imagem: Mapped[str] = mapped_column(String(256))

    persBase: Mapped[List["PersonagemBase"]] = db.relationship(
        "PersonagemBase", 
        back_populates="raca", 
        cascade="all, delete-orphan", 
        passive_deletes=True)

#Raça: (Nome, cor, desc, poderBase, imagem)