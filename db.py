from sqlmodel import create_engine

DATABASE_URL = "sqlite:///mascotas.db"

engine = create_engine(DATABASE_URL, echo=True)