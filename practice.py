from models import *
from sqlalchemy import or_, and_, not_, func


''' Select all members from User table '''
''' Raw SQL : SELECT * FROM users; '''
db_user = session.query(User).all()


''' Select Indians from table '''
''' Raw SQL : SELECT * FROM users WHERE country = 'India'; '''
# db_user = session.query(User).filter(User.country == 'India').all()


''' Select users with salary greater than 55000 '''
''' Raw SQL : SELECT * FROM users WHERE salary > 55000; '''
# db_user = session.query(User).filter(User.salary > 55000).all()


''' Select Indians and salary greater than 55000 '''
''' Raw SQL : SELECT * FROM users WHERE country = 'India' AND salary > 55000; '''
# db_user = session.query(User).filter(and_(User.country == 'India', User.salary > 55000)).all()


''' Select users with name starting with Ali '''
''' Raw SQL : SELECT * FROM users WHERE name ILIKE 'Ali%'; '''
# db_user = session.query(User).filter(User.name.ilike('Ali%')).all()


''' Select users with less than 26 or greater than 29 '''
''' Raw SQL : SELECT * FROM users WHERE age < 26 OR age > 29; '''
# db_user = session.query(User).filter(or_(User.age < 26, User.age > 29)).all()


''' Select inactive users '''
''' Raw SQL : SELECT * FROM users WHERE is_active = false; '''
# db_user = session.query(User).filter(User.is_active == False).all()


''' Select active users from India '''
''' Raw SQL : SELECT * FROM users WHERE is_active = true AND country = 'India'; '''
# db_user = session.query(User).filter(and_(User.is_active == True, User.country == 'India')).all()


''' Select users who joined after 2022-01-01 '''
''' Raw SQL : SELECT * FROM users WHERE join_date > '2022-01-01'; '''
# db_user = session.query(User).filter(User.join_date > '2022-01-01').all()


''' Select users with salary between 50000 and 70000 '''
''' Raw SQL : SELECT * FROM users WHERE salary BETWEEN 50000 AND 70000; '''
# db_user = session.query(User).filter(User.salary.between(50000, 70000)).all()


''' Select users not between 25 and 30 years old '''
''' Raw SQL : SELECT * FROM users WHERE age NOT BETWEEN 25 AND 30; '''
# db_user = session.query(User).filter(~User.age.between(25, 30)).all()


''' Select users from India or USA '''
''' Raw SQL : SELECT * FROM users WHERE country IN ('India', 'USA'); '''
# db_user = session.query(User).filter(User.country.in_(['India', 'USA'])).all()


''' Select users not from India '''
''' Raw SQL : SELECT * FROM users WHERE country != 'India'; '''
# db_user = session.query(User).filter(User.country != 'India').all()


''' Select top 3 highest paid users '''
''' Raw SQL : SELECT * FROM users ORDER BY salary DESC LIMIT 3; '''
# db_user = session.query(User).order_by(User.salary.desc()).limit(3).all()


''' Select youngest user '''
''' Raw SQL : SELECT * FROM users ORDER BY age ASC LIMIT 1; '''
# db_user = session.query(User).order_by(User.age.asc()).limit(1).all()


''' Select oldest user '''
''' Raw SQL : SELECT * FROM users ORDER BY age DESC LIMIT 1; '''
# db_user = session.query(User).order_by(User.age.desc()).limit(1).all()


''' Count total number of users '''
''' Raw SQL : SELECT COUNT(*) FROM users; '''
# total_users = session.query(func.count(User.id)).scalar()
# print("Total Users:", total_users)


''' Count total active users '''
''' Raw SQL : SELECT COUNT(*) FROM users WHERE is_active = true; '''
# active_users = session.query(func.count(User.id)).filter(User.is_active == True).scalar()
# print("Active Users:", active_users)


''' Get average salary of Indian users '''
''' Raw SQL : SELECT AVG(salary) FROM users WHERE country = 'India'; '''
# avg_salary = session.query(func.avg(User.salary)).filter(User.country == 'India').scalar()
# print("Average Salary of Indians:", avg_salary)


''' Get users ordered by join date (latest first) '''
''' Raw SQL : SELECT * FROM users ORDER BY join_date DESC; '''
# db_user = session.query(User).order_by(User.join_date.desc()).all()


''' Get users with email ending with ".com" '''
''' Raw SQL : SELECT * FROM users WHERE email ILIKE '%.com'; '''
# db_user = session.query(User).filter(User.email.ilike('%.com')).all()


for user in db_user:
    print(f"{user.name} :: {user.email} :: {user.age} :: {user.country} :: {user.salary}")
