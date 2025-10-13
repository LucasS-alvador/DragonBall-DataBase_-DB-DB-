from src.config import *

class PersonagemBase(db.Model):
    __tablename__ = "PersonagemBase"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False)
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

#PersonagemBase: (Nome, Raça_id, data_nasc, sexo,  imagem)