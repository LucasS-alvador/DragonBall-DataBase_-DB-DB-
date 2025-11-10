from database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from typing import List


personagemsaga_transformacao = db.Table(
    "PersonagemSaga_Transformacao",
    db.Column("personagemsaga_id", db.Integer, db.ForeignKey("PersonagemSaga.id", ondelete="CASCADE"), primary_key=True),
    db.Column("transformacao_id", db.Integer, db.ForeignKey("Transformacao.id", ondelete="CASCADE"), primary_key=True),
)

class Transformacao(db.Model):
    __tablename__ = "Transformacao"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    cor: Mapped[str] = mapped_column(String(64))
    especial: Mapped[str] = mapped_column(String[1024])
    efeitoCol: Mapped[str] = mapped_column(String[1024])
    poderMult: Mapped[int] = mapped_column(db.Integer, nullable=False)    
    imagem: Mapped[str] = mapped_column(String(256))
    limMinutos: Mapped[int] = mapped_column(db.Integer)

    personagens = db.relationship(
        "PersonagemSaga",
        secondary=personagemsaga_transformacao,
        back_populates="transformacoes"
    )


#Transformação: (Nome, cor, poder, especial, efeitoCol, imagem, tempo_lim)