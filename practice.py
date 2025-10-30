from models import *
from sqlalchemy import or_


''' Select all members from User table''' 
db_user = session.query(User).all()


''' Select Indians from table''' 
# db_user = session.query(User).filter(User.country == 'India').all()

''' Select users with salary greater than 55000 ''' 
# db_user = session.query(User).filter(User.salary>55000).all()

''' Select Indians and  salary greater than 55000 '''  
# db_user = session.query(User).filter(User.country == 'India').filter(User.salary>55000).all()

''' Select users with name starting with Ali '''
# db_user = session.query(User).filter(User.name.ilike('Ali%')).all()

''' Select users with less than 26 or greater than 29 '''
# db_user = session.query(User).filter(or_(User.age<26,User.age>29)).all()



for user in db_user:
    print(f"{user.name} :: {user.email} :: {user.age} :: {user.country} :: {user.salary}")