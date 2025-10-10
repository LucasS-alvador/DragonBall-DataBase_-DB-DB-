from src.config import *

class Saga(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    desc: Mapped[str] = mapped_column(String(1024))
    epIni: Mapped[int] = mapped_column(db.Integer)
    epFim: Mapped[int] = mapped_column(db.Integer, nullable=False)
    obra_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("obra.id", ondelete="CASCADE"), 
                                         nullable=False)
    obra: Mapped["Obra"] = db.relationship(
        "Obra",
        back_populates="sagas",
        foreign_keys=[obra_id])
    
    persSaga: Mapped[List["PersonagemSaga"]] = db.relationship(
        "PersonagemSaga", 
        back_populates="saga", 
        cascade="all, delete-orphan", 
        passive_deletes=True)
    