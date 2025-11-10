from config import *

class Person(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    
    cars: Mapped[List["Car"]] = db.relationship(
        "Car",
        back_populates="person",
        cascade="all, delete-orphan",
        passive_deletes=True)
    