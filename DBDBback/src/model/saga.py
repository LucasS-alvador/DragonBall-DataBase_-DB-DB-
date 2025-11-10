from database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from typing import List

from sqlalchemy.orm.session import Session
from typing import Optional

class Saga(db.Model):
    __tablename__ = "Saga"
    
    # Campos obrigatórios para criação
    required_fields = ['desc', 'epIni', 'epFim', 'obra_id']
    
    id: Mapped[int] = mapped_column(primary_key=True)
    desc: Mapped[str] = mapped_column(String(1024))
    epIni: Mapped[int] = mapped_column(db.Integer)
    epFim: Mapped[int] = mapped_column(db.Integer, nullable=False)
    obra_id: Mapped[int] = mapped_column(db.Integer, 
                                         db.ForeignKey("Obra.id", ondelete="CASCADE"), 
                                         nullable=False)
    imagem: Mapped[Optional[str]] = mapped_column(String(1024), nullable=True)
    
    obra: Mapped["Obra"] = db.relationship(
        "Obra",
        back_populates="sagas",
        foreign_keys=[obra_id])
    
    persSaga: Mapped[List["PersonagemSaga"]] = db.relationship(
        "PersonagemSaga", 
        back_populates="saga", 
        cascade="all, delete-orphan", 
        passive_deletes=True)
    
    def validate(self):
        # Validar epísódios
        if self.epFim < self.epIni:
            raise ValueError(f"O episódio final ({self.epFim}) deve ser maior ou igual ao inicial ({self.epIni})")
        if self.epIni < 1:
            raise ValueError(f"O episódio inicial ({self.epIni}) deve ser maior que zero")
        
        # Validar obra
        from model.obra import Obra
        session: Session = db.session
        obra = session.get(Obra, self.obra_id)
        if not obra:
            raise ValueError(f"Obra com ID {self.obra_id} não encontrada")
        
        # Validar descrição
        if not self.desc or not self.desc.strip():
            raise ValueError("A descrição não pode estar vazia")

    