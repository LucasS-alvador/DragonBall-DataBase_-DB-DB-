from src.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from typing import List
from src.model.transformacao import personagemsaga_transformacao

class PersonagemSaga(db.Model):
    __tablename__ = "PersonagemSaga"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    poderMult: Mapped[int] = mapped_column(db.Integer)
    imagem: Mapped[str] = mapped_column(String(256))
    persBase_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("PersonagemBase.id", ondelete="CASCADE"), 
                                         nullable=False)
    saga_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("Saga.id", ondelete="CASCADE"), 
                                         nullable=False)
    
    persBase: Mapped["PersonagemBase"] = db.relationship(
        "PersonagemBase",
        back_populates = "persSaga",
        foreign_keys = [persBase_id])
    
    saga: Mapped["Saga"] = db.relationship(
        "Saga",
        back_populates = "persSaga",
        foreign_keys = [saga_id])
    
    transformacoes = db.relationship(
        "Transformacao",
        secondary = personagemsaga_transformacao,
        back_populates = "personagens",
        passive_deletes = True
    )
    
#WARNING: I DO NOT KNOW HOW TO MAKE MANY_TO_MANY btw, so it's not done yet
#it's being done inside "tranformacao" 
#PersonagemSaga: (PersonagemBase_id, Saga_id, poder, Trans_id[], imagem)