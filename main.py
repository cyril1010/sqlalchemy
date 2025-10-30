print("SQLAlchemy Tutorial")

from models import session,User

user1 = User(name="Alice", email="alice@example.com", age=25, country="India", salary=50000, is_active=True)
user2 = User(name="Bob", email="bob@example.com", age=30, country="USA", salary=70000, is_active=True)
user3 = User(name="Charlie", email="charlie@example.com", age=28, country="India", salary=60000, is_active=False)
user4 = User(name="Diana", email="diana@example.com", age=35, country="UK", salary=90000, is_active=True)
user5 = User(name="Ethan", email="ethan@example.com", age=22, country="India", salary=40000, is_active=True)

session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.add(user5)

session.commit()

db_records = session.query(User).all()

for record in db_records:
    print(record)