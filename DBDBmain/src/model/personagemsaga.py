from src.config import *

class PersonagemSaga(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    poderMult: Mapped[int] = mapped_column(db.Integer)
    imagem: Mapped[str] = mapped_column(String(256))
    persBase_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("persBase.id", ondelete="CASCADE"), 
                                         nullable=False)
    saga_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("saga.id", ondelete="CASCADE"), 
                                         nullable=False)
    
    persBase: Mapped["PersonagemBase"] = db.relationship(
        "PersonagemBase",
        back_populates="sagas",
        foreign_keys=[persBase_id])
    
    saga: Mapped["Saga"] = db.relationship(
        "Saga",
        back_populates="persSagas",
        foreign_keys=[persBase_id])
    
#WARNING: I DO NOT KNOW HOW TO MAKE MANY_TO_MANY btw, so it's not done yet
#PersonagemSaga: (PersonagemBase_id, Saga_id, poder, Trans_id[], imagem)