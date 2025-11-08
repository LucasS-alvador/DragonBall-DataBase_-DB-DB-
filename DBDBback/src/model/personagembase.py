from src.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date
from typing import List, Optional
from datetime import date

class PersonagemBase(db.Model):
    __tablename__ = "PersonagemBase"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False)
    descricao: Mapped[str] = mapped_column(String(512), nullable=True)
    dataNasc: Mapped[date] = mapped_column(Date)
    dataMorte: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    sexo: Mapped[str] = mapped_column(String(8))
    imagem: Mapped[str] = mapped_column(String(256))

    raca_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("Raca.id", ondelete="CASCADE"), 
                                         nullable=False)

    persSaga: Mapped[List["PersonagemSaga"]] = db.relationship(
        "PersonagemSaga", 
        back_populates="persBase", 
        cascade="all, delete-orphan", 
        passive_deletes=True)
    
    raca: Mapped["Raca"] = db.relationship(
        "Raca",
        back_populates="persBase",
        foreign_keys=[raca_id])
        
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'dataNasc': self.dataNasc.isoformat() if self.dataNasc else None,
            'dataMorte': self.dataMorte.isoformat() if self.dataMorte else None,
            'sexo': self.sexo,
            'imagem': self.imagem,
            'raca_id': self.raca_id
        }

#PersonagemBase: (Nome, Raça_id, data_nasc, sexo,  imagem)