from models import *
db_user=session.query(User).filter(User.age>=28).all()
print(db_user)

for user in db_user:
    print(f"{user.name}")    
