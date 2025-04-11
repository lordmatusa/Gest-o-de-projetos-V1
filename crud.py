from sqlalchemy.orm import Session
from models import Item

def criar_item(db: Session, item_data):
    item = Item(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def listar_itens(db: Session):
    return db.query(Item).all()
