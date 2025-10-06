from src.config import *

class Obra(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(64), nullable=False)
    dtIni: Mapped[date] = mapped_column(db.Date)
    dtFim: Mapped[date] = mapped_column(db.Date)
    imagem: Mapped[str] = mapped_column(db.String(250)), 

    saga: Mapped[List["Saga"]] = db.relationship(
        "Saga",
      back_populates="obras",
        cascade="all, delete-orphan",
        passive_deletes=True)