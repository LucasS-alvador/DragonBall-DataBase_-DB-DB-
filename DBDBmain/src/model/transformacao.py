from src.config import *

class Transformacao(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(256), nullable=False)
    cor: Mapped[str] = mapped_column(String(64))
    especial: Mapped[str] = mapped_column(String[1024])
    efeitoCol: Mapped[str] = mapped_column(String[1024])
    poderMult: Mapped[int] = mapped_column(db.Integer, nullable=False)    
    imagem: Mapped[str] = mapped_column(String(256))
    limMinutos: Mapped[int] = mapped_column(db.Integer)

    persSagas: Mapped[List["PersonagemSaga"]] = db.relationship(
        "PersonagemSaga", 
        back_populates="trans", 
        cascade="all, delete-orphan", 
        passive_deletes=True)
    

#Transformação: (Nome, cor, poder, especial, efeitoCol, imagem, tempo_lim)