# Setup SQL connection here

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# DATABASE_URL = "sqlite:///./database.db"
DATABASE_URL = 'postgresql://postgres:evoqins2025@localhost:5432/cyb'




engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)
    country = Column(String(50))
    salary = Column(Float)
    is_active = Column(Boolean, default=True)
    join_date = Column(Date, default=date.today)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age='{self.age}', email='{self.email}')>"

Base.metadata.create_all(bind=engine)

