DATABASE_URL = "postgresql://postgres:akzpass@localhost:5432/akshay"
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base


engine=create_engine(DATABASE_URL)

sessionlocal=sessionmaker(bind=engine)

session=sessionlocal()

base=declarative_base()

class User1(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)
    country = Column(String(50))


    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age='{self.age}', email='{self.email}')>"

base.metadata.create_all(bind=engine)