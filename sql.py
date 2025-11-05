from models import session,User
# db_user=session.query(User).filter(User.name =="Alice").first()


# db_user=session.query(User).filter(User.name == "Bob").all()
# print(db_user)

# db_user=session.query(User).filter(User.name == "Charlie").all()
# print(db_user)
#
# db_user=session.query(User).filter(User.country == "USA").all()
# db_user=session.query(User).filter(User.name.ilike("Ali%")).all()
# db_user =session.query(User).filter(User.name.ilike("Bo%")).all()
# db_user=session.query(User).filter(User.name.ilike("%lie")).all()
# db_user=session.query(User).filter(User.age>25 , User.age<30).all()
# db_user=session.query(User).filter(User.age>21 , User.age<23).all()

# db_user=session.query(User).filter(User.is_active == True).all()
# db_user=session.query(User).filter(User.is_active == False).all()
# db_user=session.query(User).filter(User.is_active == True and User.country=="India").all()
# db_user=session.query(User).filter(User.name.ilike("Dian%")).all()
db_user=session.query(User).all()
print(db_user)


