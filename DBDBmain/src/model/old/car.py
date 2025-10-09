from src.config import *

class Car(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(1024), nullable=False)
    year: Mapped[int] = mapped_column(db.Integer)
    person_id: Mapped[int] = mapped_column(db.Integer, 
                                           db.ForeignKey("person.id"), 
                                           nullable=False)
    person: Mapped["Person"] = db.relationship(
        "Person",
        back_populates="cars",
        foreign_keys=[person_id])
    